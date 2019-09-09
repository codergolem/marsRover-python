from typing import List


class Rover:
    currentCoordinates: List[int]
    currentOrientation: str
    plateauDimensions: List[int]

    def __init__(self, plateauDimensions, initialPosition):
        self.plateauDimensions = plateauDimensions
        self.currentCoordinates = [initialPosition[0], initialPosition[1]]
        self.currentOrientation = initialPosition[2]

    def move(self, movementCommands: List[str]):
        print("Doing nothing")
        # self.currentOrientation = "Empty"
        # self.currentCoordinates = [0, 0]

    def getCurrentPosition(self):
        return [self.currentCoordinates[0], self.currentCoordinates[1], self.currentOrientation]

    def turnLeft(self):
        return RoverPosition(self.currentCoordinates[0], self.currentCoordinates[1], self.currentOrientation)


class RoverPosition:
    coordinateInX: int
    coordinateInY: int
    orientation: str

    def __init__(self, coordinateInX: int, coordinateInY: int,orientation: str):
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