from mediapipe.tasks.python import vision
from mediapipe.tasks import python
MODEL_PATH = "models/hand_landmarker.task"

base_option = python.BaseOptions(

    model_asset_path = MODEL_PATH

)
options = vision.HandLandmarkerOptions(

    base_options = base_option,
    running_mode = vision.RunningMode.VIDEO,
    num_hands = 1

)
detector = vision.HandLandmarker.create_from_options(options)
print("Video hand tracker loaded successfully")
detector.close()