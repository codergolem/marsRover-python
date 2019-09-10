from typing import List
from src.roverPosition import RoverPosition


class Rover:
    plateauDimensions: List[int]
    currentPosition: RoverPosition

    def __init__(self, plateauDimensions, initialPosition: RoverPosition):
        if not self.isPositionWithinPlateauArea(plateauDimensions, initialPosition):
            raise ValueError('rover initial position out of plateau area')
        self.plateauDimensions = plateauDimensions
        self.currentPosition = initialPosition

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
        newRoverPosition = moveMappingTable.get(self.currentPosition.getOrientation(),
                                                lambda: RoverPosition(0, 0, "X"))()
        if not self.isPositionWithinPlateauArea(self.plateauDimensions, newRoverPosition):
            raise ValueError('rover cannot be driven out of plateau area')
        self.currentPosition = newRoverPosition
        return self.currentPosition

    def isPositionWithinPlateauArea(self, plateau, position: RoverPosition):
        if (position.getCoordinateInX() > plateau[0]) or (position.getCoordinateInY() > plateau[1]):
            return False
        return True
