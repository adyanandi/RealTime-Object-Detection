# main.py

import cv2
import time
from detection import YOLOModel
from tracking import DeepSORTTracker
from log_utils import log_new_object_detected, log_object_missing

# Step 1: Initialize YOLOv8 and DeepSORT
model = YOLOModel('yolov8n.pt')  # Load YOLOv8 tiny model
deepsort = DeepSORTTracker(max_age=30)  # Initialize DeepSORT tracker

# Step 2: Open video feed
cap = cv2.VideoCapture('sample.mp4')

if not cap.isOpened():
    print("Error: Could not open webcam or video.")
    exit()

# Initialize tracking info
track_id_to_class = {}        # Map track_id to class_name
detected_ids = set()          # Track detected object IDs
missing_ids = set()           # Track already-reported missing IDs

# For FPS calculation
prev_time = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # (Optional) Resize frame to speed up detection
    frame = cv2.resize(frame, (640, 480))

    # Step 3: Detect using YOLOv8
    detections, class_names = model.predict(frame, conf=0.5)

    # Step 4: Update DeepSORT
    tracks = deepsort.update(detections, frame)

    current_ids = set()
    for track in tracks:
        if not track.is_confirmed() or track.time_since_update > 1:
            continue

        x1, y1, x2, y2 = track.to_tlbr()
        track_id = track.track_id
        current_ids.add(track_id)

        # Save class name for new track ID
        if track_id not in track_id_to_class:
            # Get class name using track.det_class directly from the result
            class_name = class_names[track.det_class] if hasattr(track, 'det_class') else "Unknown"
            track_id_to_class[track_id] = class_name

        class_name = track_id_to_class.get(track_id, "Unknown")

        # Draw bounding box and label
        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 2)
        cv2.putText(frame, f"{class_name} {track_id}", (int(x1), int(y1)-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

        # New object detected
        if track_id not in detected_ids:
            detected_ids.add(track_id)
            if track_id in missing_ids:
                missing_ids.remove(track_id)  # If object reappears, remove from missing list
            log_new_object_detected(class_name, track_id)

    # Step 5: Find missing IDs
    disappeared_ids = detected_ids - current_ids

    for missing_id in disappeared_ids:
        if missing_id not in missing_ids:
            class_name = track_id_to_class.get(missing_id, "Unknown")
            log_object_missing(class_name, missing_id)
            missing_ids.add(missing_id)

    # FPS calculation
    current_time = time.time()
    fps = 1 / (current_time - prev_time)
    prev_time = current_time

    # Show FPS
    cv2.putText(frame, f"FPS: {int(fps)}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Show frame
    cv2.imwrite(f"frame_{int(time.time())}.jpg", frame)

    # Break loop on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up
cap.release()
cv2.destroyAllWindows()



















