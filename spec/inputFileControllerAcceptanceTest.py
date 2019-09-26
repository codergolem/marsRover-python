import pytest
from src.inputFileController import InputFileController
from src.rover import Rover

def test_shouldCalculateFinalPositionForTwoRovers(capsys):
    # Given
    inputFilePath = 'testFiles/inputFile.txt'
    inputFileController = InputFileController()
    # When
    inputFileController.processFile(inputFilePath)
    printedOutput = capsys.readouterr().out
    # Then
    expectedRoversFinalPositions = '1 3 N' + '\n' + '5 1 E' + '\n'
    assert expectedRoversFinalPositions == printedOutput
