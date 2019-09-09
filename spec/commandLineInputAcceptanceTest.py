import builtins

from src.commandLineInput import CommandLineInput

class Test_MarsRoverAcceptanceTest:

    instructionsSequenceCounter = 0

    def mockedCompleteInstructionsSequence(self):
        mockedInput = ""

        if self.instructionsSequenceCounter == 0:
            mockedInput = "5 5"
        if self.instructionsSequenceCounter == 1:
            mockedInput = "1,2,N"
        if self.instructionsSequenceCounter == 2:
            mockedInput = "LMLMLMLMM"
        # if self.instructionsSequenceCounter == 3:
        #     mockedInput = "n"
        self.instructionsSequenceCounter += 1
        return mockedInput

    def test_canMoveOneRoverToFinalPosition(self, capsys):
        # Given
        commandLineInput = CommandLineInput()
        samplePlateauDimension = "5 5"
        # When
        builtins.input = self.mockedCompleteInstructionsSequence
        commandLineInput.startReceivingCommands()
        lastPrintedOutput = capsys.readouterr().out
        # Then
        expectedRoverFinalPosition = "3 3 E"
        assert lastPrintedOutput == expectedRoverFinalPosition + "\n"
        assert commandLineInput.getPlateauDimension() == samplePlateauDimension
