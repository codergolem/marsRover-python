from mock import patch, mock_open
from marsrover.inputfilecontroller import InputFileController
from marsrover.parser import Parser

class Test_InputFileController:

    parser = Parser()

    def test_shouldCalculateFinalPositionForOneRover(self, capsys):
        # Given
        filePath = 'somePathToFile/file.txt'
        mockedFileContent = '5 5\n3 3 E\nMMRMMRMRRM'

        # When
        with patch('builtins.open', mock_open(read_data=mockedFileContent)):
            inputFileController = InputFileController()
            inputFileController.processFile(filePath, self.parser)

        # Then
        printedOutput = capsys.readouterr().out
        lastPrintedLine = printedOutput.replace('\n', '')
        expectedFinalPosition = "5 1 E"
        assert lastPrintedLine == expectedFinalPosition

    def test_shouldCalculateFinalPositionForThreeeRovers(self, capsys):
        # Given
        filePath = 'somePathToFile/file.txt'
        mockedFileContent = '5 5\n3 3 E\nMMRMMRMRRM\n2 2 N\nMRMLM\n1 1 N\nM'

        inputFileController2 = InputFileController()

        # When
        with patch('builtins.open', mock_open(read_data=mockedFileContent)):
            inputFileController2.processFile(filePath, self.parser)

        # Then
        printedOutput = capsys.readouterr().out
        expectedFinalPosition = "5 1 E\n3 4 N\n1 2 N\n"
        assert printedOutput == expectedFinalPosition

    def test_shouldPrintAnErrorWhenPlateauDimensionsAreNotValid(self, capsys):
        # Given
        filePath = 'somePathToFile/file.txt'
        mockedFileContent = 's 5\n3 3 E\nMMRMMRMRRM\n2 2 N\nMRMLM\n1 1 N\nM'

        inputFileController = InputFileController()

        # When
        with patch('builtins.open', mock_open(read_data=mockedFileContent)):
            inputFileController.processFile(filePath, self.parser)

        # Then
        printedOutput = capsys.readouterr().out
        errorMessage = "Invalid plateau dimensions\n"
        assert printedOutput == errorMessage

    def test_shouldPrintAnErrorWhenRoverInitialPositionIsNotValid(self, capsys):
        # Given
        filePath = 'somePathToFile/file.txt'
        mockedFileContent = '5 5\n3 s E\nMMRMMRMRRM\n2 2 N\nMRMLM\n1 1 N\nM'

        inputFileController = InputFileController()

        # When
        with patch('builtins.open', mock_open(read_data=mockedFileContent)):
            inputFileController.processFile(filePath, self.parser)

        # Then
        printedOutput = capsys.readouterr().out
        errorMessage = "Invalid rover initial position\n"
        assert printedOutput == errorMessage

    def test_shouldPrintAnErrorWhenRoverInitialOrientationIsNotValid(self, capsys):
        # Given
        filePath = 'somePathToFile/file.txt'
        mockedFileContent = '5 5\n3 3 X\nMMRMMRMRRM\n2 2 N\nMRMLM\n1 1 N\nM'

        inputFileController = InputFileController()

        # When
        with patch('builtins.open', mock_open(read_data=mockedFileContent)):
            inputFileController.processFile(filePath, self.parser)

        # Then
        printedOutput = capsys.readouterr().out
        errorMessage = "'X' is not a valid Orientation\n"
        assert printedOutput == errorMessage

    def test_shouldPrintAnErrorWhenAnMovementCommandIsNotValid(self, capsys):
        # Given
        filePath = 'somePathToFile/file.txt'
        mockedFileContent = '5 5\n3 3 E\nMMRXMRMRRM\n2 2 N\nMRMLM\n1 1 N\nM'

        inputFileController = InputFileController()

        # When
        with patch('builtins.open', mock_open(read_data=mockedFileContent)):
            inputFileController.processFile(filePath, self.parser)

        # Then
        printedOutput = capsys.readouterr().out
        errorMessage = "'X' is not a valid MovementCommand\n"
        assert printedOutput == errorMessage
