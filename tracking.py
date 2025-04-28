# tracking.py

from deep_sort_realtime.deepsort_tracker import DeepSort

class DeepSORTTracker:
    def __init__(self, max_age=30):
        """
        Initialize DeepSORT Tracker.
        :param max_age: Maximum age for tracking (number of frames before disappearance)
        """
        self.deepsort = DeepSort(max_age=max_age)

    def update(self, detections, frame):
        """
        Update the tracker with new detections.
        :param detections: List of detections [(x1, y1, x2, y2), confidence, class_id]
        :param frame: Current video frame
        :return: Tracks information
        """
        return self.deepsort.update_tracks(detections, frame=frame)
