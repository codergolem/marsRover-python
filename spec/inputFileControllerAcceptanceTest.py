import pytest
from src.inputFileController import InputFileController
from src.rover import Rover

def test_shouldCalculateFinalPositionForTwoRovers(capsys):
    # Given
    inputFilePath = 'testFiles/inputFile.txt'
    inputFileController = InputFileController()
    # When
    inputFileController.executeCommands(inputFilePath)
    printedOutput = capsys.readouterr().out.replace('\n', '')
    # Then
    expectedRoversFinalPositions = '1 3 N' + '\n' + '5 1 E' + '\n'
    assert expectedRoversFinalPositions == printedOutput


  with patch('builtins.open', mock_open(read_data='foo\nbar\nbaz\n')):
            inputFileController = InputFileController()
            inputFileController.processFile(filePath)
