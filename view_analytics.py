from analytics import WorkoutAnalytics
analytics = WorkoutAnalytics(log_dir="workout_logs")

analytics.summary()

analytics.plot_progress()

analytics.plot_avg_speed()