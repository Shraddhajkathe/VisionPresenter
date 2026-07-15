import cv2

from modules.vision.hand_detector import HandDetector


class Camera:

    def __init__(self):

        self.camera = cv2.VideoCapture(0)

        self.detector = HandDetector()

    def start(self):

        while True:

            success, frame = self.camera.read()

            if not success:
                break

            frame = self.detector.detect(frame)

            cv2.imshow("VisionPresenter", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        self.camera.release()

        cv2.destroyAllWindows()