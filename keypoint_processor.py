

class KeypointProcessor:
    def __init__(self):
        pass

    def process(self, kpts):
        pose_points = {
        "left_shoulder":  (kpts[5][0], kpts[5][1]),
        "right_shoulder": (kpts[6][0], kpts[6][1]),

        "left_elbow":     (kpts[7][0], kpts[7][1]),
        "right_elbow":    (kpts[8][0], kpts[8][1]),

        "left_wrist":     (kpts[9][0], kpts[9][1]),
        "right_wrist":    (kpts[10][0], kpts[10][1]),

        "left_hip":       (kpts[11][0], kpts[11][1]),
        "right_hip":      (kpts[12][0], kpts[12][1]),

        "left_knee":      (kpts[13][0], kpts[13][1]),
        "right_knee":     (kpts[14][0], kpts[14][1]),

        "left_ankle":     (kpts[15][0], kpts[15][1]),
        "right_ankle":    (kpts[16][0], kpts[16][1])
        }

        return pose_points