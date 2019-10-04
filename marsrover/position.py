from marsrover.orientation import Orientation


class RoverPosition:

    def __init__(self, coordinateInX: int, coordinateInY: int, orientation: Orientation):
        self.coordinateInX: int = coordinateInX
        self.coordinateInY: int = coordinateInY
        self.orientation: Orientation = orientation

    def toString(self) -> str:
        return str(self.coordinateInX) + " " + str(self.coordinateInY) + " " + self.orientation.value
