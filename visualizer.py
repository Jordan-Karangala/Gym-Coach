import cv2
from feedback_engine import FeedbackEngine
from overlay_renderer import OverlayRenderer
from rolling_feedback import RollingFeedback


class Visualizer:

    def __init__(self, config):
        self.config = config
        self.feedback_engine = FeedbackEngine(config)
        self.overlay = OverlayRenderer(config)
        self.rolling_feedback = RollingFeedback(config)

    def draw(self, frame, rep_result, feedback,  exercise_name, key_points=None,):

        if rep_result is None:
            return frame

        # =========================
        # Draw ONLY ACTIVE SIDE angle skeleton
        # =========================
        if key_points is not None and rep_result is not None:

            active_side = rep_result.get("active_side")

            angle_definition = self.config.get("angle_definition")

            if active_side and angle_definition:

                joints = angle_definition.get(active_side)

                if joints and len(joints) == 3:

                    A_name, B_name, C_name = joints

                    A = key_points.get(A_name)
                    B = key_points.get(B_name)
                    C = key_points.get(C_name)

                    LINE_COLOR = (0, 255, 255)
                    POINT_COLOR = (0, 255, 0)

                    if A is not None and B is not None:
                        cv2.line(
                            frame,
                            (int(A[0]), int(A[1])),
                            (int(B[0]), int(B[1])),
                            LINE_COLOR,
                            4
                        )

                    if B is not None and C is not None:
                        cv2.line(
                            frame,
                            (int(B[0]), int(B[1])),
                            (int(C[0]), int(C[1])),
                            LINE_COLOR,
                            4
                        )

                    # draw angle points
                    for point in [A, B, C]:

                        if point is not None:
                            cv2.circle(
                                frame,
                                (int(point[0]), int(point[1])),
                                6,
                                POINT_COLOR,
                                -1
                            )

        rep_count = rep_result["rep_count"]
        state = rep_result["current_state"]
        angle = rep_result["active_angle"]
        speed = rep_result["rep_speed_state"]
        extended = self.config["angle_thresholds"]["extended"]
        flexed = self.config["angle_thresholds"]["flexed"]

        progress = None

        if angle is not None:
            progress = (angle - flexed) / (extended - flexed)

            # clamp between 0 and 1
            progress = max(0.0, min(1.0, progress))
        y = 40

        cv2.putText(frame, f"Reps: {rep_count}",
                    (30, y),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0,255,0),
                    2)

        y += 40

        cv2.putText(frame, f"State: {state}",
                    (30, y),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (255,255,0),
                    2)

        y += 40

        if angle is not None:
            cv2.putText(frame, f"Angle: {int(angle)}",
                        (30, y),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8,
                        (255,255,255),
                        2)

        y += 40

        if speed is not None:
            cv2.putText(frame, f"Speed: {speed}",
                        (30, y),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8,
                        (0,165,255),
                        2)

        frame = self.overlay.draw_progress_bar(frame, angle)
        rolling_feedback = self.rolling_feedback.get_feedback(rep_result)
        final_feedback = feedback if feedback else rolling_feedback
        frame = self.overlay.draw_feedback(frame, final_feedback)

        return frame