import os
import glob
import pandas as pd
import matplotlib.pyplot as plt


class WorkoutAnalytics:

    def __init__(self, log_dir="workout_logs"):

        self.log_dir = log_dir
        self.df = self._load_all_logs()

        if self.df is not None and not self.df.empty:

            self.df["timestamp"] = pd.to_datetime(self.df["timestamp"])
            self.df["date"] = self.df["timestamp"].dt.date


    # ---------------------------------------------------
    # Load all CSV files
    # ---------------------------------------------------

    def _load_all_logs(self):

        files = glob.glob(os.path.join(self.log_dir, "*.csv"))

        if not files:
            print("No workout logs found.")
            return None

        df_list = []

        for file in files:
            df = pd.read_csv(file)
            df_list.append(df)

        return pd.concat(df_list, ignore_index=True)


    # ---------------------------------------------------
    # Total reps per session (per day)
    # ---------------------------------------------------

    def total_reps_per_session(self):

        if self.df is None:
            return

        reps = self.df.groupby("date")["rep_count"].max()

        print("\nTotal reps per session:\n")
        print(reps)

        return reps


    # ---------------------------------------------------
    # Average rep speed (numeric)
    # ---------------------------------------------------

    def average_rep_duration(self):

        if self.df is None:
            return

        avg = self.df.groupby("date")["rep_duration"].mean()

        print("\nAverage rep duration (seconds):\n")
        print(avg)

        return avg


    # ---------------------------------------------------
    # Speed category distribution
    # ---------------------------------------------------

    def speed_distribution(self):

        if self.df is None:
            return

        dist = self.df["rep_speed"].value_counts()

        print("\nSpeed distribution:\n")
        print(dist)

        return dist


    # ---------------------------------------------------
    # Progress graph — reps per day
    # ---------------------------------------------------

    def plot_progress(self):

        if self.df is None:
            return

        reps = self.df.groupby("date")["rep_count"].max()

        plt.figure()

        plt.plot(reps.index, reps.values, marker="o")

        plt.title("Workout Progress (Reps per Session)")
        plt.xlabel("Date")
        plt.ylabel("Total Reps")

        plt.grid()

        plt.show()


    # ---------------------------------------------------
    # Average speed graph
    # ---------------------------------------------------

    def plot_avg_speed(self):

        if self.df is None:
            return

        avg_speed = self.df.groupby("date")["rep_duration"].mean()

        plt.figure()

        plt.plot(avg_speed.index, avg_speed.values, marker="o")

        plt.title("Average Rep Duration Progress")
        plt.xlabel("Date")
        plt.ylabel("Seconds")

        plt.grid()

        plt.show()


    # ---------------------------------------------------
    # Full summary
    # ---------------------------------------------------

    def summary(self):

        print("\n========== WORKOUT SUMMARY ==========")

        self.total_reps_per_session()

        self.average_rep_duration()

        self.speed_distribution()

        print("=====================================\n")