from src.rover import Rover
from src.position import RoverPosition
from src.orientation import Orientation
from src.plateau import Plateau
from src.movementcommand import MovementCommand
import pytest


class Test_Rover:

    def test_RoverCanMoveToPosition(self):
        # Given
        initialPosition = RoverPosition(2, 2, Orientation.NORTH)
        plateau = Plateau(5, 5)
        movementCommands = [MovementCommand.FORWARD,
                            MovementCommand.RIGHT,
                            MovementCommand.FORWARD,
                            MovementCommand.LEFT,
                            MovementCommand.FORWARD]
        rover = Rover(plateau, initialPosition)
        # When
        rover.processCommands(movementCommands)
        # Then
        expectedFinalPosition = '3 4 N'
        assert rover.getCurrentPosition().toString() == expectedFinalPosition

    def test_CannotCreateRoverIfInitialPositionOutOfPlateauArea(self):
        # Given
        plateau = Plateau(5, 5)
        initialPosition = RoverPosition(6, 5, Orientation.NORTH)
        # Then
        with pytest.raises(ValueError, match='rover initial position out of plateau area'):
            rover = Rover(plateau, initialPosition)

    def test_CannotMoveRoverOutOfPlateau(self):
        # Given
        initialPosition = RoverPosition(2, 2, Orientation.NORTH)
        plateau = Plateau(3, 3)
        movementCommands = [MovementCommand.FORWARD, MovementCommand.FORWARD, MovementCommand.FORWARD]
        rover = Rover(plateau, initialPosition)
        # Then
        with pytest.raises(ValueError, match='rover cannot be driven out of plateau area'):
            rover.processCommands(movementCommands)
        assert rover.getCurrentPosition().toString() == RoverPosition(2, 3, Orientation.NORTH).toString()
