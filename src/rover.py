from typing import List
from src.position import RoverPosition
from src.plateau import Plateau
from src.orientation import Orientation
from src.movementcommand import MovementCommand


class Rover:

    def __init__(self, plateau, initialPosition: RoverPosition):
        if not self.isPositionWithinPlateauArea(plateau, initialPosition):
            raise ValueError('rover initial position out of plateau area')
        self.plateau = plateau
        self.currentPosition = initialPosition

    def processCommands(self, commands: List[MovementCommand]):

        for command in commands:
            if command == MovementCommand.FORWARD:
                self.move()
            if command == MovementCommand.RIGHT:
                self.turnRight()
            if command == MovementCommand.LEFT:
                self.turnLeft()

    def getCurrentPosition(self) -> RoverPosition:
        return self.currentPosition

    def turnLeft(self):
        leftOrientationMapping = {
            Orientation.NORTH: Orientation.WEST,
            Orientation.WEST: Orientation.SOUTH,
            Orientation.SOUTH: Orientation.EAST,
            Orientation.EAST: Orientation.NORTH
        }
        newOrientation = leftOrientationMapping.get(self.currentPosition.getOrientation(), "X")
        newPosition = RoverPosition(self.currentPosition.getCoordinateInX(),
                                    self.currentPosition.getCoordinateInY(),
                                    newOrientation)
        self.currentPosition = newPosition
        return newPosition

    def turnRight(self):
        rightOrientationMapping = {
            Orientation.NORTH: Orientation.EAST,
            Orientation.WEST: Orientation.NORTH,
            Orientation.SOUTH: Orientation.WEST,
            Orientation.EAST: Orientation.SOUTH
        }
        newOrientation = rightOrientationMapping.get(self.currentPosition.getOrientation(), "X")
        newPosition = RoverPosition(self.currentPosition.getCoordinateInX(),
                                    self.currentPosition.getCoordinateInY(),
                                    newOrientation)
        self.currentPosition = newPosition
        return newPosition

    def move(self):
        moveMappingTable = {
            Orientation.NORTH: lambda: RoverPosition(self.currentPosition.getCoordinateInX(),
                                                     self.currentPosition.getCoordinateInY() + 1,
                                                     self.currentPosition.getOrientation()),
            Orientation.SOUTH: lambda: RoverPosition(self.currentPosition.getCoordinateInX(),
                                                     self.currentPosition.getCoordinateInY() - 1,
                                                     self.currentPosition.getOrientation()),
            Orientation.WEST: lambda: RoverPosition(self.currentPosition.getCoordinateInX() - 1,
                                                    self.currentPosition.getCoordinateInY(),
                                                    self.currentPosition.getOrientation()),
            Orientation.EAST: lambda: RoverPosition(self.currentPosition.getCoordinateInX() + 1,
                                                    self.currentPosition.getCoordinateInY(),
                                                    self.currentPosition.getOrientation())
        }
        newRoverPosition = moveMappingTable.get(self.currentPosition.getOrientation(),
                                                lambda: RoverPosition(0, 0, Orientation.SOUTH))()
        if not self.isPositionWithinPlateauArea(self.plateau, newRoverPosition):
            raise ValueError('rover cannot be driven out of plateau area')
        self.currentPosition = newRoverPosition
        return self.currentPosition

    def isPositionWithinPlateauArea(self, plateau, position: RoverPosition):
        if (position.getCoordinateInX() > plateau.getDimensionInX()) or (
                position.getCoordinateInY() > plateau.getDimensionInY()):
            return False
        return True
