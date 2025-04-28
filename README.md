# Real-Time Detection of Object (Missing and New Object Placement) 

This project focuses on real-time object detection and tracking, using advanced computer vision techniques to detect, identify, and monitor objects from a live video feed.
It also measures system performance by calculating the Frames Per Second (FPS) during runtime.

The system detects when objects appear and disappear, assigns unique IDs, and logs events for analysis.




## Features

- **Real-Time Object Detection**: Continuously detects objects from a live video stream using a YOLOv10-based model, ensuring quick and accurate recognition.

- **New Object Identification**: Instantly recognizes and reports when a new object appears in the frame, along with its assigned unique ID and class label.

- **Missing Object Detection**: Detects when an object disappears from the frame and logs the missing object's ID and class.

- **Frame-by-Frame Monitoring**: Continuously monitors every frame for object appearance and disappearance to maintain up-to-date tracking.

- **FPS Monitoring**: Calculates and displays the average FPS (frames per second) over recent frames to evaluate real-time performance.

- **Efficient ID Assignment**: Assigns unique IDs to each detected object to ensure accurate tracking across frames.

- **Console Logging**: Provides clear, timestamped logs for new and missing objects, along with FPS updates, for easy tracking and debugging.

- **Performance Optimization**: Optimized pipeline for maintaining stable detection even on lower FPS environments (~4-6 FPS observed).

- **Lightweight and Scalable**: Designed for efficient operation on different hardware setups, supporting scalability for larger real-time systems.



## Tech Stack

- **Python**: Primary programming language for building the application logic, object detection, tracking, and managing real-time performance.

- **OpenCV**: Used for video frame capture, real-time processing, and displaying results with bounding boxes and labels.

- **YOLOv8**: Pre-trained object detection model for accurately detecting and classifying objects in real-time video streams.

- **DeepSORT**: A tracking algorithm used to maintain object identities across frames and track new/missing objects in the real-time feed.



## Installation

Clone the repository

```bash
git clone https://github.com/adyanandi/RealTime-Object-Detection
cd realTime-Object-Detection
```
Create a virtual environment (optional but recommended):
```bash
pip install pipenv
```
```bash
pipenv shell
```
```bash
pipenv install
```
Install Requirements
```bash
pip install -r requirements.txt
```
Run the application
```bash 
python run main.py
```


    
## Docker Setup(Optional)

Build the Docker Image
```bash
docker build -t object-tracking-app .
```
Run the Docker Container
```bash
docker run -v /path/to/your/project:/app -it object-tracking-app:latest
```
