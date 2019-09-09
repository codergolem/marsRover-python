from src.rover import Rover
from src.rover import RoverPosition

class Test_Rover:

    def test_RoverCanMoveToPosition(self):
        # Given
        initialPosition = [2, 2, "N"]
        plateau = [5, 5]
        movementCommands = ["M", "R", "M"]
        rover = Rover(plateau,initialPosition)
        rover.move(movementCommands)
        expectedFinalPosition = [3, 3, "E"]
        assert rover.getCurrentPosition() == expectedFinalPosition

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