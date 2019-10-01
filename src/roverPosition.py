from src.orientation import Orientation


class RoverPosition:
    coordinateInX: int
    coordinateInY: int
    orientation: Orientation

    def __init__(self, coordinateInX: int, coordinateInY: int, orientation: Orientation):
        self.coordinateInX = coordinateInX
        self.coordinateInY = coordinateInY
        self.orientation = orientation

    def getCoordinateInX(self) -> int:
        return self.coordinateInX

    def getCoordinateInY(self) -> int:
        return self.coordinateInY

    def getOrientation(self) -> Orientation:
        return self.orientation

    def toString(self) -> str:
        return str(self.coordinateInX) + " " + str(self.coordinateInY) + " " + self.orientation.value