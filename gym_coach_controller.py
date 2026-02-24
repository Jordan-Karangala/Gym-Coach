from config import EXERCISE_CONFIGS
from person_detector import PersonDetector
from keypoint_processor import KeypointProcessor
from angle_calculator import AngleCalculator, SideLocker
from rep_counter import RepCounter
from visualizer import Visualizer
from workout_logger import WorkoutLogger
from feedback_engine import FeedbackEngine


class GymCoachController:

    def __init__(self, exercise_name):
        self.config = EXERCISE_CONFIGS.get(exercise_name)
        # print(self.config)
        self.person_detector = PersonDetector()
        self.keypoint_processor = KeypointProcessor()
        self.angle_calculator = AngleCalculator(exercise_name=exercise_name)
        self.side_locker = SideLocker()
        self.rep_counter = RepCounter(self.config)
        self.feedback_engine = FeedbackEngine(self.config)
        self.visualizer = Visualizer(self.config)
        self.logger = WorkoutLogger(self.config)
        self.last_feedback = None


        # self.feedback_generator = FeedbackGenerator()
        # self.display = Display()


    def process_frame(self, frame, exercise_name):

        # Step 1: detect people
        boxes, kpts = self.person_detector.detect_people(frame)
        if kpts is None:
            return frame
        # Step 2: process keypoints
        key_points = self.keypoint_processor.process(kpts)
        # Step 3: calculate angles
        left_angle_current, right_angle_current = self.angle_calculator.calculate_angle(key_points)
        print(f"left: {left_angle_current} right: {right_angle_current}")
        side_result = self.side_locker.update(left_angle_current,right_angle_current)
        active_side = side_result["active_side"]
        active_angle = side_result["active_angle"]
        side_locked = side_result["side_locked"]
        # # Step 5: count reps
        previous_count = self.rep_counter.rep_count
        rep_result = self.rep_counter.rep_update(side_result)
        feedback = None
        if self.rep_counter.rep_count > previous_count:
            feedback = self.feedback_engine.get_feedback(
                exercise_name,
                rep_result,
                self.config.get("form_targets")
            )
            print("LLM returned:", feedback)  # Can be removed after debugging
            if feedback:
                self.last_feedback = feedback

        # updating logger file and generate feedback
            self.logger.log_rep(
                exercise_name,
                rep_result,
                self.rep_counter.min_angle_reached,
                self.rep_counter.max_angle_reached
            )

        frame = self.visualizer.draw(
            frame,
            rep_result,
            self.last_feedback,
            exercise_name,
            key_points
        )
        print(rep_result) # Can be removed after debugging
        return frame

        #
        # # Step 7: display
        # self.display.show(frame, feedback, rep_data)


    def select_main_person(self, people):

        if len(people) == 0:
            return None

        return people[0]
