from modules.vision.motion_tracker import MotionTracker
from modules.vision.landmark_manager import LandmarkManager
from src.core.action_manager import ActionManager
import cv2
import mediapipe as mp

from modules.vision.gesture_recognition import GestureRecognizer


class HandDetector:

    def __init__(self):

        self.mpHands = mp.solutions.hands

        self.hands = self.mpHands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )

        self.drawer = mp.solutions.drawing_utils
        self.gesture = GestureRecognizer()
        self.motion = MotionTracker()
        self.landmark_manager = LandmarkManager()
        self.action = ActionManager()
        
    def detect(self, frame):

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = self.hands.process(rgb)

        if results.multi_hand_landmarks:

            for hand in results.multi_hand_landmarks:

                self.drawer.draw_landmarks(
                    frame,
                    hand,
                    self.mpHands.HAND_CONNECTIONS
                )

                gesture = self.gesture.recognize(hand)

                points = self.landmark_manager.get_landmarks(hand, frame)

                h, w, _ = frame.shape

                cx, cy = points[9]
                direction = self.motion.get_direction(cx, cy)
                action = self.action.update(
                     gesture,
                    direction
                )
                cv2.putText(
                    frame,
                    f"{gesture} | {direction} | {action}",
                    (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0),
                    2
                )

        return frame