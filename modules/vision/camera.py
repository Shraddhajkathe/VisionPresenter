import cv2

from modules.vision.hand_detector import HandDetector


class Camera:

    def __init__(self):

        self.cap = cv2.VideoCapture(0)

        if not self.cap.isOpened():
            raise Exception("Cannot open webcam.")

        self.detector = HandDetector()

    def start(self):

        while True:

            success, frame = self.cap.read()

            if not success:
                break

            frame = self.detector.detect(frame)

            cv2.imshow("VisionPresenter", frame)

            key = cv2.waitKey(1)

            if key == ord("q"):
                break

        self.cap.release()
        cv2.destroyAllWindows()