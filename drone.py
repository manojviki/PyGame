from datetime import datetime

class Drone:
    """Defines the Drone class."""

    def __init__(self, name="drone", x_position=0, y_position=0, power=100, radius=15, colour=[255,255,255], thickness=3):
        self.name = name
        self.x = x_position
        self.y = y_position
        self.p = power
        self.r = radius
        self.c = colour
        self.t = thickness

    def move(self, direction):
        """Moves the drone, if within safe limits."""

        if direction=="up":
            self.y -= 1
            self.p -= .02
        elif direction=="down":
            self.y += 1
            self.p -= .02
        elif direction == "left":
            self.x -= 1
            self.p -= .02
        elif direction=="right":
            self.x += 1
            self.p -= .02
        else:
            return False

        return True

    def report(self):
        """Reports on the location and battery level."""
        date = datetime.now()
        text = "Report from " + self.name + " @ " + str(date) + ": "
        text += "bat=" + str(round(self.p,2)) + "%, "
        text += "lon=" + str(self.y) + ", "
        text += "lat=" + str(self.x) + ", "
        text += "alt=" + str(self.p) + "."
        return text
