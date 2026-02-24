class RollingFeedback:

    def __init__(self, config):
        self.config = config
        self.targets = config.get("form_targets", {})

    def get_feedback(self, rep_result):

        if rep_result is None:
            return None

        angle = rep_result.get("active_angle")
        state = rep_result.get("current_state")
        speed = rep_result.get("rep_speed_state")

        if angle is None:
            return None

        ideal_extended = self.targets.get("ideal_extended")
        ideal_flexed = self.targets.get("ideal_flexed")

        # ==========================
        # DEPTH / EXTENSION FEEDBACK
        # ==========================

        if state == "flexed" and ideal_flexed is not None:
            if angle > ideal_flexed + 10:
                return "Go lower"

        if state == "extended" and ideal_extended is not None:
            if angle < ideal_extended - 10:
                return "Fully extend"

        # ==========================
        # SPEED FEEDBACK
        # ==========================

        if speed == "fast":
            return "Slow down"

        if speed == "slow":
            return "Move slightly faster"

        return None