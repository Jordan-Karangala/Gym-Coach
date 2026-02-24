from ultralytics import YOLO
import numpy as np
model_path = "yolov8m-pose.pt"
class PersonDetector:
    def __init__(self):
        self.frame = None
        self.model = YOLO(model_path)



    def detect_people(self, frame):
        self.frame = frame
        a, b, c, current_angle = None, None, None, None
        results = self.model(self.frame)
        # print(f"Actual resutls from model:", results)
        if results[0].boxes and len(results[0].boxes) > 0:
            boxes = results[0].boxes.xyxy.cpu().numpy()
            if len(boxes) == 0:
                return None
            areas = [(b[2] - b[0]) * (b[3] - b[1]) for b in boxes]
            main_user_idx = np.argmax(areas)
            person_height = boxes[main_user_idx][3] - boxes[main_user_idx][1]
            kpts = results[0].keypoints.xy[main_user_idx].cpu().numpy()
            # print(f"Person_height: {person_height} \n KeyPoints: {kpts}")
            return boxes, kpts