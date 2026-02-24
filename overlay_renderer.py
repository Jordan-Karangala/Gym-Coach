import cv2

class OverlayRenderer:

    def __init__(self, config):

        self.extended = config["angle_thresholds"]["extended"]
        self.flexed = config["angle_thresholds"]["flexed"]

    def draw_progress_bar(self, frame, angle):

        if angle is None:
            return frame

        progress = (angle - self.flexed) / (self.extended - self.flexed)
        progress = max(0, min(1, progress))

        bar_x = 30
        bar_y = 200
        bar_width = 300
        bar_height = 20

        filled = int(bar_width * progress)

        # background
        cv2.rectangle(frame,
                      (bar_x, bar_y),
                      (bar_x + bar_width, bar_y + bar_height),
                      (50,50,50),
                      -1)

        # filled
        cv2.rectangle(frame,
                      (bar_x, bar_y),
                      (bar_x + filled, bar_y + bar_height),
                      (0,255,0),
                      -1)

        return frame

    def draw_feedback(self, frame, feedback):

        if not feedback:
            return frame

        cv2.putText(frame,
                    feedback,
                    (30, 260),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.9,
                    (0,255,255),
                    2)

        return frame