import builtins
from src.commandlinecontroller import CommandLineController


class Test_MarsRoverAcceptanceTest:

    instructionsSequenceCounter = 0
    plateau = ''
    initialPosition = ''
    commands = ''

    def mockedCompleteInstructionsSequence(self):
        mockedInput = ""

        if self.instructionsSequenceCounter == 0:
            mockedInput = self.plateau
        if self.instructionsSequenceCounter == 1:
            mockedInput = self.initialPosition
        if self.instructionsSequenceCounter == 2:
            mockedInput = self.commands
        self.instructionsSequenceCounter += 1
        return mockedInput

    def test_canMoveOneRoverToFinalPosition(self, capsys):
        # Given
        commandLine = CommandLineController()
        self.plateau = "5 5"
        self.initialPosition = "3 3 E"
        self.commands = "MMRMMRMRRM"
        # When
        builtins.input = self.mockedCompleteInstructionsSequence
        commandLine.startReceivingCommands()
        printedOutput = capsys.readouterr().out.split("Final Position: ")
        lastPrintedLine = printedOutput[-1].replace('\n', '')
        # Then
        expectedRoverFinalPosition = "5 1 E"
        assert lastPrintedLine == expectedRoverFinalPosition

    def test_shouldInformUserAndStartOverWhenInitialPositionBeyondPlateau(self, capsys):
        # Given
        commandLine = CommandLineController()
        self.plateau = "5 5"
        self.initialPosition = "6 3 E"
        self.commands = "MMRMMRMRRM"
        # When
        builtins.input = self.mockedCompleteInstructionsSequence
        commandLine.startReceivingCommands()
        printedOutput = capsys.readouterr().out
        expectedErrorMessage = 'invalid input: rover out of plateau area'
        if expectedErrorMessage in printedOutput:
            assert True
        else:
            assert False
