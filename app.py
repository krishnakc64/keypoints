import cv2
import time
from keypoint_detector import KeypointDetector


# COCO keypoint skeleton connections
SKELETON = [
    (5, 7), (7, 9),       # left arm
    (6, 8), (8, 10),      # right arm
    (5, 6),               # shoulders
    (5, 11), (6, 12),     # body
    (11, 12),             # hips
    (11, 13), (13, 15),   # left leg
    (12, 14), (14, 16)    # right leg
]


def draw_cyberpunk_ui(frame, fps, person_count):
    h, w = frame.shape[:2]

    yellow = (0, 255, 255)
    cyan = (255, 255, 0)
    green = (0, 255, 0)
    pink = (255, 0, 255)
    white = (255, 255, 255)
    dark = (20, 20, 20)

    cv2.rectangle(frame, (10, 10), (w - 10, 75), dark, 2)

    cv2.putText(
        frame,
        "CYBERPUNK KEYPOINT DETECTION",
        (25, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.75,
        yellow,
        2
    )

    cv2.rectangle(frame, (10, 95), (350, 245), dark, 2)

    cv2.putText(frame, "STATUS: RUNNING",
                (25, 130),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                green,
                2)

    cv2.putText(frame, "MODEL: YOLOv8 Pose",
                (25, 165),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                cyan,
                2)

    cv2.putText(frame, f"PERSONS: {person_count}",
                (25, 200),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                white,
                2)

    cv2.putText(frame, f"FPS: {fps:.2f}",
                (25, 235),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                yellow,
                2)

    scan_y = int((time.time() * 100) % h)
    cv2.line(frame, (0, scan_y), (w, scan_y), pink, 1)

    return frame


def draw_keypoints(frame, detections):
    for det in detections:
        x1, y1, x2, y2 = det["box"]
        keypoints = det["keypoints"]

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 255), 2)

        cv2.putText(
            frame,
            f"person {det['conf']:.2f}",
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 255),
            2
        )

        # Draw keypoint dots
        for kp in keypoints:
            x, y = int(kp[0]), int(kp[1])

            if x > 0 and y > 0:
                cv2.circle(frame, (x, y), 4, (0, 255, 0), -1)

        # Draw skeleton lines
        for p1, p2 in SKELETON:
            x1_kp, y1_kp = int(keypoints[p1][0]), int(keypoints[p1][1])
            x2_kp, y2_kp = int(keypoints[p2][0]), int(keypoints[p2][1])

            if x1_kp > 0 and y1_kp > 0 and x2_kp > 0 and y2_kp > 0:
                cv2.line(
                    frame,
                    (x1_kp, y1_kp),
                    (x2_kp, y2_kp),
                    (255, 0, 255),
                    2
                )

    return frame


def run_app():
    detector = KeypointDetector()

    cap = cv2.VideoCapture(0)

    last_time = time.time()

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Camera not detected.")
            break

        detections = detector.detect(frame)

        frame = draw_keypoints(frame, detections)

        current_time = time.time()
        fps = 1.0 / max(current_time - last_time, 0.0001)
        last_time = current_time

        frame = draw_cyberpunk_ui(frame, fps, len(detections))

        cv2.imshow("Keypoint Detection UI", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run_app()