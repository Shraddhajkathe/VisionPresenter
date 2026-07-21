class ActionManager:

    def __init__(self):
        self.current_action = "NONE"

    def update(self, gesture, direction):

        if gesture == "OPEN PALM":

            # YOUR movement:
            # RIGHT → LEFT
            if direction == "LEFT":
                self.current_action = "NEXT_SLIDE"

            # YOUR movement:
            # LEFT → RIGHT
            elif direction == "RIGHT":
                self.current_action = "PREVIOUS_SLIDE"

            else:
                self.current_action = "NONE"

        elif gesture == "ANNOTATION":
            self.current_action = "ANNOTATION"

        elif gesture == "FIST":
            self.current_action = "NONE"

        return self.current_action