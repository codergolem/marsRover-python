from typing import List
from marsrover.plateau import Plateau
from marsrover.position import RoverPosition
from marsrover.orientation import Orientation
from marsrover.movementcommand import MovementCommand


class Rover:

    def __init__(self, plateau: Plateau, initialPosition: RoverPosition):
        if not self.isPositionWithinPlateauArea(plateau, initialPosition):
            raise ValueError('rover initial position out of plateau area')
        self.plateau: Plateau = plateau
        self.currentPosition: RoverPosition = initialPosition

    def processCommands(self, commands: List[MovementCommand]):

        for command in commands:
            if command == MovementCommand.FORWARD:
                self.move()
            if command == MovementCommand.RIGHT:
                self.turnRight()
            if command == MovementCommand.LEFT:
                self.turnLeft()

    def turnLeft(self) -> RoverPosition:
        leftOrientationMapping = {
            Orientation.NORTH: Orientation.WEST,
            Orientation.WEST: Orientation.SOUTH,
            Orientation.SOUTH: Orientation.EAST,
            Orientation.EAST: Orientation.NORTH
        }
        newOrientation = leftOrientationMapping.get(self.currentPosition.orientation, Orientation.NORTH)
        newPosition = RoverPosition(self.currentPosition.coordinateInX,
                                    self.currentPosition.coordinateInY,
                                    newOrientation)
        self.currentPosition = newPosition
        return newPosition

    def turnRight(self) -> RoverPosition:
        rightOrientationMapping = {
            Orientation.NORTH: Orientation.EAST,
            Orientation.WEST: Orientation.NORTH,
            Orientation.SOUTH: Orientation.WEST,
            Orientation.EAST: Orientation.SOUTH
        }
        newOrientation = rightOrientationMapping.get(self.currentPosition.orientation, Orientation.NORTH)
        newPosition = RoverPosition(self.currentPosition.coordinateInX,
                                    self.currentPosition.coordinateInY,
                                    newOrientation)
        self.currentPosition = newPosition
        return newPosition

    def move(self) -> RoverPosition:
        moveMappingTable = {
            Orientation.NORTH: lambda: RoverPosition(self.currentPosition.coordinateInX,
                                                     self.currentPosition.coordinateInY + 1,
                                                     self.currentPosition.orientation),
            Orientation.SOUTH: lambda: RoverPosition(self.currentPosition.coordinateInX,
                                                     self.currentPosition.coordinateInY - 1,
                                                     self.currentPosition.orientation),
            Orientation.WEST: lambda: RoverPosition(self.currentPosition.coordinateInX - 1,
                                                    self.currentPosition.coordinateInY,
                                                    self.currentPosition.orientation),
            Orientation.EAST: lambda: RoverPosition(self.currentPosition.coordinateInX + 1,
                                                    self.currentPosition.coordinateInY,
                                                    self.currentPosition.orientation)
        }
        newRoverPosition = moveMappingTable.get(self.currentPosition.orientation,
                                                lambda: RoverPosition(0, 0, Orientation.SOUTH))()
        if not self.isPositionWithinPlateauArea(self.plateau, newRoverPosition):
            raise ValueError('rover cannot be driven out of plateau area')
        self.currentPosition = newRoverPosition
        return self.currentPosition

    def isPositionWithinPlateauArea(self, plateau: Plateau, position: RoverPosition):
        if (position.coordinateInX > plateau.dimensionInX or
                position.coordinateInY > plateau.dimensionInY):
            return False
        return True
