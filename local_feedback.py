class LocalFeedback:

    def __init__(self):
        pass

    def get_feedback(self, exercise_name, rep_result):

        if rep_result is None:
            return ""

        speed = rep_result.get("rep_speed_state")
        state = rep_result.get("current_state")
        angle = rep_result.get("active_angle")
        rep_in_progress = rep_result.get("rep_in_progress")

        # Priority 1 — speed feedback
        if speed == "fast":
            return "Slow down"

        if speed == "slow":
            return "Move faster"

        if speed == "good":
            return "Good pace"

        # Priority 2 — position feedback
        if state == "flexed":
            return "Good depth"

        if state == "extended":
            return "Fully extended"

        # Priority 3 — rep phase feedback
        if rep_in_progress:
            return "Keep going"

        # default fallback
        return "Ready"