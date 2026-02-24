import os
os.environ["HF_HUB_READ_TIMEOUT"] = "300"
import cv2
from gym_coach_controller import GymCoachController

def open_video_source(source=0):
    """
    Opens video source.
    source can be:
        0       → webcam
        1       → external webcam
        "file.mp4" → video file
    """
    cap = cv2.VideoCapture(source)

    if not cap.isOpened():
        raise RuntimeError(f"Cannot open video source: {source}")

    return cap


def get_frame_delay(cap, default_fps=30):
    """
    Calculates delay between frames in milliseconds.
    This keeps playback speed correct.
    Webcam sometimes returns FPS = 0,
    so we use default_fps in that case.
    """
    fps = cap.get(cv2.CAP_PROP_FPS)

    if fps <= 0 or fps != fps:  # fps != fps checks for NaN
        fps = default_fps

    delay = int(1000 / fps)

    return delay, fps


def play_video(source, detector,  exercise_name,  window_name="Video Player"):
    """
    Main function to play video or webcam.
    source:
        0 = webcam
        "file.mp4" = video file
    """
    # Open video source
    cap = open_video_source(source)

    # Get correct delay between frames
    delay, fps = get_frame_delay(cap)

    print(f"Video opened successfully")
    print(f"FPS: {fps:.2f}")
    print("Press 'q' to exit")

    while True:
        # Read one frame
        ret, frame = cap.read()

        # If no frame → video ended OR webcam disconnected
        if not ret:
            print("Video ended or cannot receive frame.")
            break

        annotated_frame = detector.process_frame(frame, exercise_name)
        # Show frame
        cv2.imshow(window_name, annotated_frame)

        # waitKey does 3 important things:
        # 1. Displays image
        # 2. Controls playback speed
        # 3. Detects keyboard input
        key = cv2.waitKey(delay) & 0xFF

        # Exit if user presses 'q'
        if key == ord('q'):
            print("User exited.")
            break

    # Release camera/video
    cap.release()

    # Close all windows
    cv2.destroyAllWindows()

    print("Resources released. Program ended cleanly.")


# =========================
# SELECT SOURCE HERE
# =========================
exercise_name = "bicep_curl"        # "squat"# 'bicep_curl' # 'lunge'  # 'pushup'
video_path = "bicep_curl_videos/14858245_2160_3840_60fps.mp4"
if __name__ == "__main__":

    frame_processor = GymCoachController(exercise_name=exercise_name)
    # Option 1: Webcam
    # play_video(source=0)

    # Option 2: External webcam
    # play_video(source=1)

    # Option 3: Video file path
    play_video(source=video_path,
               detector = frame_processor,
               exercise_name=exercise_name)

