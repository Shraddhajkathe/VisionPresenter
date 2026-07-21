class GestureRecognizer:

    def __init__(self):
        pass

    def recognize(self, hand):

        landmarks = hand.landmark

        index_tip = landmarks[8]
        index_pip = landmarks[6]

        middle_tip = landmarks[12]
        middle_pip = landmarks[10]

        ring_tip = landmarks[16]
        ring_pip = landmarks[14]

        pinky_tip = landmarks[20]
        pinky_pip = landmarks[18]

        fingers = []

        fingers.append(index_tip.y < index_pip.y)
        fingers.append(middle_tip.y < middle_pip.y)
        fingers.append(ring_tip.y < ring_pip.y)
        fingers.append(pinky_tip.y < pinky_pip.y)

        if fingers == [True, False, False, False]:
            return "ANNOTATION"

        elif fingers == [True, True, True, True]:
            return "OPEN PALM"

        elif fingers == [False, False, False, False]:
            return "FIST"

        else:
            return "UNKNOWN"