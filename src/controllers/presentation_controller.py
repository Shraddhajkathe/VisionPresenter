import pyautogui
import time


class PresentationController:

    def __init__(self):

        self.last_action_time = 0
        self.cooldown = 1.0      # seconds

    def execute(self, action):

        current_time = time.time()

        if current_time - self.last_action_time < self.cooldown:
            return

        if action == "NEXT_SLIDE":

            pyautogui.press("right")
            print("➡ NEXT SLIDE")

            self.last_action_time = current_time

        elif action == "PREVIOUS_SLIDE":

            pyautogui.press("left")
            print("⬅ PREVIOUS SLIDE")

            self.last_action_time = current_time