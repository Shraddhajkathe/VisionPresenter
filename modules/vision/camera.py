import cv2


class Camera:

    def __init__(self):
        self.camera = cv2.VideoCapture(0)

    def start(self):

        while True:

            success, frame = self.camera.read()

            if not success:
                print("Unable to access camera.")
                break

            cv2.imshow("VisionPresenter - Camera", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        self.camera.release()
        cv2.destroyAllWindows()