# detection.py

from ultralytics import YOLO

class YOLOModel:
    def __init__(self, model_path):
        """
        Initialize the YOLO model.
        :param model_path: Path to the YOLO model file (e.g., yolov8n.pt)
        """
        self.model = YOLO(model_path)

    def predict(self, frame, conf=0.5):
        """
        Perform prediction on a single frame.
        :param frame: The input frame (image)
        :param conf: Confidence threshold for detections
        :return: detections (list of tuples), class_names (list)
        """
        results = self.model.predict(source=frame, conf=conf, stream=True, verbose=False)

        detections = []
        class_names = None
        for result in results:
            boxes = result.boxes.xyxy.cpu().numpy()
            class_ids = result.boxes.cls.cpu().numpy().astype(int)
            confidences = result.boxes.conf.cpu().numpy()
            class_names = result.names  # Get class names

            for box, class_id, confidence in zip(boxes, class_ids, confidences):
                x1, y1, x2, y2 = box
                detections.append(((x1, y1, x2, y2), confidence, class_id))  # Include class_id

        return detections, class_names
