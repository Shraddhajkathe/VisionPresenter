class MotionTracker:

    def __init__(self):

        self.previous_x = None
        self.previous_y = None

    def get_direction(self, x, y):

        if self.previous_x is None:

            self.previous_x = x
            self.previous_y = y

            return "NONE"

        dx = x - self.previous_x
        dy = y - self.previous_y

        self.previous_x = x
        self.previous_y = y

        threshold = 20

        if abs(dx) < threshold and abs(dy) < threshold:
            return "STILL"

        if abs(dx) > abs(dy):

            if dx > 0:
                return "RIGHT"

            else:
                return "LEFT"

        else:

            if dy > 0:
                return "DOWN"

            else:
                return "UP"