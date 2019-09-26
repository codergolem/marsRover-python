from mock import patch, mock_open
from src.inputFileController import InputFileController

class Test_InputFileController:

    def test_shouldCalculateFinalPositionForOneRover(self, mocker, capsys):
        # Given
        filePath = 'somePathToFile/file.txt'
        mockedFileContent = '5 5\n3 3 E\nMMRMMRMRRM'

        # When
        with patch('builtins.open', mock_open(read_data=mockedFileContent)):
            inputFileController = InputFileController()
            inputFileController.processFile(filePath)

        # Then
        printedOutput = capsys.readouterr().out
        lastPrintedLine = printedOutput.replace('\n', '')
        expectedFinalPosition = "5 1 E"
        assert lastPrintedLine == expectedFinalPosition


    def test_shouldCalculateFinalPositionForThreeeRovers(self, mocker, capsys):
        # Given
        filePath = 'somePathToFile/file.txt'
        mockedFileContent = '5 5\n3 3 E\nMMRMMRMRRM\n2 2 N\nMRMLM\n1 1 N\nM'

        inputFileController2 = InputFileController()

        # When
        with patch('builtins.open', mock_open(read_data=mockedFileContent)):
            inputFileController2.processFile(filePath)

        # Then
        printedOutput = capsys.readouterr().out
        expectedFinalPosition = "5 1 E\n3 4 N\n1 2 N\n"
        assert printedOutput == expectedFinalPosition