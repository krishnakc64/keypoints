# Keypoint Detection System using Pose Estimation (Jetson Nano)

## Project Overview
This project is a **Keypoint Detection System** built using real-time pose estimation.  
It detects human body keypoints from a live camera feed and visualizes the **human skeleton structure**.

The system:
- Detects human body joints (keypoints)
- Draws skeleton connections
- Displays results in real-time
- Shows UI with FPS and person count

---

## Objective
To build a real-time keypoint detection system using:
- Computer vision (OpenCV)
- Pose estimation (YOLOv8 Pose model)
- Live camera feed on Jetson Nano

---

## Technologies Used
- Python 3  
- OpenCV  
- Ultralytics YOLOv8 (Pose Model)  
- Jetson Nano  
- USB Camera  

---

## Keypoint Detection
In this project:
- The model detects human body joints such as:
  - Shoulders  
  - Elbows  
  - Wrists  
  - Hips  
  - Knees  
  - Ankles  

- These keypoints are connected to form a **skeleton structure**

---

## Project Structure
keypoint_detector.py → Keypoint detection logic  
app.py → Camera UI + keypoint visualization  
screenshots/ → Output images  

---

## How to Run

### 1. Install dependencies
```bash
pip3 install opencv-python numpy ultralytics
```
---
### 2. Create files

Create the following files in your project folder:

- `keypoint_detector.py` → contains keypoint detection logic  
- `app.py` → contains webcam UI and visualization  

---

### 3. Run the project

```bash
python3 app.py
```
---
## Output Examples

### Normal Detection
- Human detected  
- Keypoints plotted  
- Skeleton drawn  
- Status: SYSTEM RUNNING  

---

## Features
- Real-time keypoint detection  
- Human skeleton visualization  
- Live camera feed  
- FPS display  
- Person count detection  
- CyberPunk UI overlay  

---

## Results

### Keypoint Detection Output
<img width="1024" height="600" alt="Screenshot from 2026-04-28 22-45-54" src="https://github.com/user-attachments/assets/6674eb60-c046-41ee-9869-bfedc6451b56" />
<img width="1024" height="600" alt="Screenshot from 2026-04-28 22-44-25" src="https://github.com/user-attachments/assets/4c694fb1-a592-4f5f-9ed1-56a7e04503f8" />


---

## Notes
- The YOLOv8 pose model (`yolov8n-pose.pt`) is downloaded automatically  
- Screenshots are captured manually from the live output  
- Designed to run efficiently on Jetson Nano  

---

## Conclusion

The project successfully demonstrates real-time human keypoint detection using pose estimation.  
It provides a clear visualization of body movements and enhances understanding of human pose analysis using computer vision.
