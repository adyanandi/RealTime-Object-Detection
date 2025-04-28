# log_utils.py

from utils import get_timestamp

def log_new_object_detected(class_name, track_id):
    """
    Log the detection of a new object.
    :param class_name: Name of the detected object
    :param track_id: ID of the detected object
    """
    print(f"{get_timestamp()} New object detected: {class_name} with ID: {track_id}")

def log_object_missing(class_name, track_id):
    """
    Log the missing status of an object.
    :param class_name: Name of the object
    :param track_id: ID of the object
    """
    print(f"{get_timestamp()} Object missing: {class_name} with ID {track_id}")
