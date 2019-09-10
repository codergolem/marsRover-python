from src.rover import Rover
from src.rover import RoverPosition
import pytest

class Test_Rover:

    def test_RoverCanMoveToPosition(self):
        # Given
        initialPosition = RoverPosition(2, 2, "N")
        plateau = [5, 5]
        movementCommands = ["M", "R", "M", "L", "M"]
        rover = Rover(plateau, initialPosition)
        # When
        rover.processCommands(movementCommands)
        # Then
        expectedFinalPosition = '3 4 N'
        assert rover.getCurrentPosition().toString() == expectedFinalPosition

    def test_CannotCreateRoverIfInitialPositionOutOfPlateauArea(self):
        # Given
        plateau = [5, 5]
        initialPosition = RoverPosition(6, 5, 'N')
        # Then
        with pytest.raises(ValueError, match='rover initial position out of plateau area'):
            rover = Rover(plateau, initialPosition)

