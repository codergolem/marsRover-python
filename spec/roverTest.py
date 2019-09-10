from src.rover import Rover
import pytest

class Test_Rover:

    def test_RoverCanMoveToPosition(self):
        # Given
        initialPosition = [2, 2, "N"]
        plateau = [5, 5]
        movementCommands = ["M", "R", "M", "L", "M"]
        rover = Rover(plateau, initialPosition)
        # When
        rover.processCommands(movementCommands)
        # Then
        expectedFinalPosition = '3 4 N'
        assert rover.getCurrentPosition().toString() == expectedFinalPosition

    def test_CannotCreateRoverIfInitialPositionOutOfPlateauArea(self):
        print("test")
        # Given
        plateau = [5, 5]
        initialPosition = [6, 5, 'N']
        # Then
        with pytest.raises(ValueError, match='rover initial position out of plateau area'):
            rover = Rover(plateau, initialPosition)

