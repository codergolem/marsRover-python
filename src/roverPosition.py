class RoverPosition:
    coordinateInX: int
    coordinateInY: int
    orientation: str

    def __init__(self, coordinateInX: int, coordinateInY: int, orientation: str):
        self.coordinateInX = coordinateInX
        self.coordinateInY = coordinateInY
        self.orientation = orientation

    def getCoordinateInX(self) -> int:
        return self.coordinateInX

    def getCoordinateInY(self) -> int:
        return self.coordinateInY

    def getOrientation(self) -> str:
        return self.orientation

    def toString(self) -> str:
        return str(self.coordinateInX) + " " + str(self.coordinateInY) + " " + self.orientation