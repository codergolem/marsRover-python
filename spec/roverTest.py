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
