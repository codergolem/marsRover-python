from src.rover import Rover
from src.rover import RoverPosition


class Test_Rover:

    def test_RoverCanMoveToPosition(self):
        # Given
        initialPosition = [2, 2, "N"]
        plateau = [5, 5]
        movementCommands = ["M", "R", "M", "L", "M"]
        rover = Rover(plateau, initialPosition)
        rover.processCommands(movementCommands)
        expectedFinalPosition = '3 4 N'
        assert rover.getCurrentPosition().toString() == expectedFinalPosition

    def test_RoverTurnLeft(self):
        #Given
        initialPosition = [2, 2, "N"]
        plateau = [5, 5]
        rover = Rover(plateau, initialPosition)
        # When
        currentRoverPosition: RoverPosition = rover.turnLeft()
        # Then
        expectedRoverPosition = RoverPosition(2, 2, "W")
        assert currentRoverPosition.toString() == expectedRoverPosition.toString()
