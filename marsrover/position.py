from marsrover.orientation import Orientation


class RoverPosition:
    coordinateInX: int
    coordinateInY: int
    orientation: Orientation

    def __init__(self, coordinateInX: int, coordinateInY: int, orientation: Orientation):
        self.coordinateInX = coordinateInX
        self.coordinateInY = coordinateInY
        self.orientation = orientation

    def toString(self) -> str:
        return str(self.coordinateInX) + " " + str(self.coordinateInY) + " " + self.orientation.value