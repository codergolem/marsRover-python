from marsrover.instruction import RoverInstruction
from marsrover.instruction import RoverPosition
from marsrover.orientation import Orientation
from marsrover.movementcommand import MovementCommand


class Test_RoverInstruction:

    def test_shouldReturnInstructionAsString(self):
        # Given
        instruction = RoverInstruction(RoverPosition(2, 2, Orientation.NORTH),
                                       [MovementCommand.FORWARD, MovementCommand.LEFT])
        expectedInstructionAsString = '2 2 N' + '\n' + 'ML'
        # When
        result = instruction.toString()
        # Then
        assert  result == expectedInstructionAsString
