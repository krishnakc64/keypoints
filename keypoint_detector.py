from ultralytics import YOLO


class KeypointDetector:
    def __init__(self):
        # YOLOv8 pose model for human keypoints
        self.model = YOLO("/home/krishna/Desktop/jetson_labs/yolov8n-pose.pt")

    def detect(self, frame):
        results = self.model(frame, verbose=False)

        detections = []

        for r in results:
            if r.keypoints is None:
                continue

            boxes = r.boxes
            keypoints = r.keypoints.xy

            for i in range(len(keypoints)):
                conf = float(boxes.conf[i]) if boxes is not None else 0.0

                x1, y1, x2, y2 = map(int, boxes.xyxy[i])

                person_keypoints = keypoints[i].cpu().numpy()

                detections.append({
                    "conf": conf,
                    "box": (x1, y1, x2, y2),
                    "keypoints": person_keypoints
                })

        return detections