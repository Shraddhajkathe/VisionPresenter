class LandmarkManager:

    def get_landmarks(self, hand, frame):

        h, w, _ = frame.shape

        lm = hand.landmark

        points = {}

        for i, landmark in enumerate(lm):

            x = int(landmark.x * w)
            y = int(landmark.y * h)

            points[i] = (x, y)

        return points