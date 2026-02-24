import time

class RepCounter:
    def __init__(self, config):
        self.config = config
        self.active_angle = None
        self.side_locked = False

        self.rep_count = 0

        self.previous_angle = None

        self.min_angle_reached = None
        self.max_angle_reached = None

        self.rep_in_progress = False

        self.current_state = None
        self.previous_state = None

        self.rep_start_time = None
        self.rep_end_time = None
        self.rep_duration = None
        self.rep_speed_state = None


    def rep_update(self, side_result):

        # Step 0 — update side lock and angle
        self.side_locked = side_result["side_locked"]
        active_angle = side_result["active_angle"]
        self.active_angle = active_angle

        if not self.side_locked or active_angle is None:
            rep_result = {
                "rep_count": self.rep_count,
                "current_state": self.current_state,
                "active_angle": self.active_angle,
                "rep_duration": self.rep_duration,
                "rep_speed_state": self.rep_speed_state,
                "rep_in_progress": self.rep_in_progress,
                "min_angle": self.min_angle_reached,
                "max_angle": self.max_angle_reached
            }
            return rep_result

        # Step 1 — initialize baseline (first frame)

        if self.previous_angle is None:

            self.previous_angle = active_angle

            self.min_angle_reached = active_angle
            self.max_angle_reached = active_angle
            self.previous_state = self.current_state

            rep_result = {
                "rep_count": self.rep_count,
                "current_state": self.current_state,
                "active_angle": self.active_angle,
                "rep_duration": self.rep_duration,
                "rep_speed_state": self.rep_speed_state,
                "rep_in_progress": self.rep_in_progress,
                "min_angle": self.min_angle_reached,
                "max_angle": self.max_angle_reached
            }
            return rep_result


        # Step 2 — update min and max angles reached
        if active_angle < self.min_angle_reached:
            self.min_angle_reached = active_angle

        if active_angle > self.max_angle_reached:
            self.max_angle_reached = active_angle


        # Step 3 — read thresholds from config
        extended_threshold = self.config["angle_thresholds"]["extended"]
        flexed_threshold = self.config["angle_thresholds"]["flexed"]
        min_range_required = self.config["angle_thresholds"]["min_range"]


        # Step 4 — detect current state
        if active_angle >= extended_threshold:
            self.current_state = "extended"

        elif active_angle <= flexed_threshold:
            self.current_state = "flexed"

        else:
            self.current_state = "mid_range"

        if self.previous_angle is None:
            self.previous_angle = active_angle

            self.min_angle_reached = active_angle
            self.max_angle_reached = active_angle

            self.previous_state = self.current_state

            return {
                "rep_count": self.rep_count,
                "current_state": self.current_state,
                "active_angle": self.active_angle,
                "rep_duration": self.rep_duration,
                "rep_speed_state": self.rep_speed_state,
                "rep_in_progress": self.rep_in_progress,
                "active_side": side_result["active_side"],
                "min_angle": self.min_angle_reached,
                "max_angle": self.max_angle_reached
            }
        print("DEBUG:", "previous_state =",
              self.previous_state, "current_state =", self.current_state)
        # Step 5 — detect rep start
        if self.previous_state != "flexed" and self.current_state == "flexed":

            self.rep_in_progress = True
            self.rep_start_time = time.time()


        # Step 6 — detect rep completion
        if self.rep_in_progress and self.current_state == "extended" and self.previous_state != "extended":

            angle_range = self.max_angle_reached - self.min_angle_reached

            if angle_range >= min_range_required:

                # FIRST record end time
                self.rep_end_time = time.time()

                # THEN calculate duration
                self.rep_duration = self.rep_end_time - self.rep_start_time

                # Speed classification
                speed_fast = self.config["speed_thresholds"]["fast"]
                speed_slow = self.config["speed_thresholds"]["slow"]

                if self.rep_duration < speed_fast:
                    self.rep_speed_state = "fast"

                elif self.rep_duration > speed_slow:
                    self.rep_speed_state = "slow"

                else:
                    self.rep_speed_state = "good"

                # Count rep
                self.rep_count += 1

                # Reset for next rep
            self.rep_in_progress = False
            self.min_angle_reached = active_angle
            self.max_angle_reached = active_angle


        # Step 7 — update previous values
        self.previous_angle = active_angle
        self.previous_state = self.current_state
        rep_result = {
            "rep_count": self.rep_count,
            "current_state": self.current_state,
            "active_angle": self.active_angle,
            "rep_duration": self.rep_duration,
            "rep_speed_state": self.rep_speed_state,
            "rep_in_progress": self.rep_in_progress,
            "active_side": side_result["active_side"],
            "min_angle": self.min_angle_reached,
            "max_angle": self.max_angle_reached
        }
        return rep_result
