from config import EXERCISE_CONFIGS
import numpy as np

class SideLocker:

    def __init__(self, movement_threshold=20.0, lock_frames_required=5):

        # previous angles
        self.left_angle_previous = None
        self.right_angle_previous = None

        # accumulated movement
        self.left_movement_score = 0.0
        self.right_movement_score = 0.0

        # threshold to decide lock
        self.movement_threshold = movement_threshold

        # number of frames to observe before locking
        self.lock_frames_required = lock_frames_required
        self.frame_counter = 0

        # lock state
        self.side_locked = False
        self.active_side = None

        # current active angle
        self.active_angle = None


    def update(self, left_angle_current, right_angle_current):

        # safety check
        if left_angle_current is None or right_angle_current is None:

            return {
                "active_side": self.active_side,
                "active_angle": self.active_angle,
                "side_locked": self.side_locked,
                "left_movement_score": self.left_movement_score,
                "right_movement_score": self.right_movement_score
            }


        # initialize previous angles first frame
        if self.left_angle_previous is None:
            self.left_angle_previous = left_angle_current

        if self.right_angle_previous is None:
            self.right_angle_previous = right_angle_current


        # calculate movement this frame
        left_movement = abs(left_angle_current - self.left_angle_previous)
        right_movement = abs(right_angle_current - self.right_angle_previous)


        # accumulate movement if not locked
        if not self.side_locked:

            self.left_movement_score += left_movement
            self.right_movement_score += right_movement

            self.frame_counter += 1


            # check lock condition after sufficient frames
            if self.frame_counter >= self.lock_frames_required:

                if (self.left_movement_score >= self.movement_threshold or
                    self.right_movement_score >= self.movement_threshold):


                    if self.left_movement_score > self.right_movement_score:

                        self.active_side = "left"
                        self.active_angle = left_angle_current

                    else:

                        self.active_side = "right"
                        self.active_angle = right_angle_current


                    self.side_locked = True


        # if already locked, just update active angle
        else:

            if self.active_side == "left":
                self.active_angle = left_angle_current

            else:
                self.active_angle = right_angle_current


        # update previous angles
        self.left_angle_previous = left_angle_current
        self.right_angle_previous = right_angle_current


        return {
            "active_side": self.active_side,
            "active_angle": self.active_angle,
            "side_locked": self.side_locked,
            "left_movement_score": self.left_movement_score,
            "right_movement_score": self.right_movement_score,

        }

class AngleCalculator:
    def __init__(self, exercise_name):
        self.config = EXERCISE_CONFIGS.get(exercise_name)
        self.exercise_name = exercise_name

    def _calculate_angle_between_points(self, A, B, C):

        import numpy as np

        A = np.array(A)
        B = np.array(B)
        C = np.array(C)

        BA = A - B
        BC = C - B

        cosine_angle = np.dot(BA, BC) / (
                np.linalg.norm(BA) * np.linalg.norm(BC)
        )

        angle = np.degrees(np.arccos(cosine_angle))

        return angle



    def calculate_angle(self, key_points):

        if len(key_points) <= 6:
            return None, None

        angle_def = self.config.get("angle_definition")

        if not angle_def:
            print(f"Config Error: No angle_definition for {self.exercise_name}")
            return None, None

        # LEFT SIDE
        left_A_name, left_B_name, left_C_name = angle_def["left"]

        left_A = key_points.get(left_A_name)
        left_B = key_points.get(left_B_name)
        left_C = key_points.get(left_C_name)

        left_angle_current = None

        if left_A and left_B and left_C:
            left_angle_current = self._calculate_angle_between_points(
                left_A, left_B, left_C
            )

        # RIGHT SIDE
        right_A_name, right_B_name, right_C_name = angle_def["right"]

        right_A = key_points.get(right_A_name)
        right_B = key_points.get(right_B_name)
        right_C = key_points.get(right_C_name)

        right_angle_current = None

        if right_A and right_B and right_C:
            right_angle_current = self._calculate_angle_between_points(
                right_A, right_B, right_C
            )

        return left_angle_current, right_angle_current

