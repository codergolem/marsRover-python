from typing import List
from src.roverPosition import RoverPosition


class Rover:

    plateauDimensions: List[int]
    currentPosition: RoverPosition

    # TODO: Validate initial position according to Plateau dimensions
    def __init__(self, plateauDimensions, initialPosition):
        if not self.isPositionWithinPlateauArea(plateauDimensions, initialPosition):
            raise ValueError('rover initial position out of plateau area')
        self.plateauDimensions = plateauDimensions
        self.currentPosition = RoverPosition(initialPosition[0], initialPosition[1], initialPosition[2])

    def processCommands(self, commands: List[str]):

        for command in commands:
            if command == 'M':
                self.move()
            if command == 'R':
                self.turnRight()
            if command == 'L':
                self.turnLeft()

    def getCurrentPosition(self) -> RoverPosition:
        return self.currentPosition

    def turnLeft(self):
        leftOrientationMapping = {
            "N": "W",
            "W": "S",
            "S": "E",
            "E": "N"
        }
        newOrientation = leftOrientationMapping.get(self.currentPosition.getOrientation(), "X")
        newPosition = RoverPosition(self.currentPosition.getCoordinateInX(),
                                    self.currentPosition.getCoordinateInY(),
                                    newOrientation)
        self.currentPosition = newPosition
        return newPosition

    def turnRight(self):
        rightOrientationMapping = {
            "N": "E",
            "W": "N",
            "S": "W",
            "E": "S"
        }
        newOrientation = rightOrientationMapping.get(self.currentPosition.getOrientation(), "X")
        newPosition = RoverPosition(self.currentPosition.getCoordinateInX(),
                                    self.currentPosition.getCoordinateInY(),
                                    newOrientation)
        self.currentPosition = newPosition
        return newPosition

    def move(self):
        moveMappingTable = {
            "N": lambda: RoverPosition(self.currentPosition.getCoordinateInX(),
                                       self.currentPosition.getCoordinateInY() + 1,
                                       self.currentPosition.getOrientation()),
            "S": lambda: RoverPosition(self.currentPosition.getCoordinateInX(),
                                       self.currentPosition.getCoordinateInY() - 1,
                                       self.currentPosition.getOrientation()),
            "W": lambda: RoverPosition(self.currentPosition.getCoordinateInX() - 1,
                                       self.currentPosition.getCoordinateInY(),
                                       self.currentPosition.getOrientation()),
            "E": lambda: RoverPosition(self.currentPosition.getCoordinateInX() + 1,
                                       self.currentPosition.getCoordinateInY(),
                                       self.currentPosition.getOrientation())
        }
        calculateNewRoverPosition = moveMappingTable.get(self.currentPosition.getOrientation(), lambda: RoverPosition(0, 0, "X"))
        self.currentPosition = calculateNewRoverPosition()
        return self.currentPosition

    def isPositionWithinPlateauArea(self, plateau, position):
        if (position[0] > plateau[0]) or (position[1] > plateau[1]):
            return False
        return True

