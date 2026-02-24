import csv
import os
import datetime


class WorkoutLogger:

    def __init__(self, config):
        self.config = config
        log_dir = config["logging"]["log_dir"]
        os.makedirs(log_dir, exist_ok=True)
        today = datetime.date.today().isoformat()
        self.file_path = os.path.join(log_dir, f"{today}.csv")
        self._initialize_file()


    def _initialize_file(self):
        if not os.path.exists(self.file_path):
            with open(self.file_path, mode="w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([
                    "timestamp",
                    "exercise",
                    "rep_count",
                    "rep_duration",
                    "rep_speed",
                    "min_angle",
                    "max_angle"
                ])


    def log_rep(self, exercise_name, rep_result, min_angle, max_angle):
        if rep_result["rep_duration"] is None:
            return

        timestamp = datetime.datetime.now().isoformat()
        with open(self.file_path, mode="a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                timestamp,
                exercise_name,
                rep_result["rep_count"],
                rep_result["rep_duration"],
                rep_result["rep_speed_state"],
                min_angle,
                max_angle
            ])