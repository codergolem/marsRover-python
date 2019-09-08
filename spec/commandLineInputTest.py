import pytest
from src.commandLineInput import *

def test_canProvidePlateauDimensions(capsys):
    # Given
    commandLineInput = CommandLineInput()
    # When
    commandLineInput.startReceivingCommands()

    # Then
    printedOutput = capsys.readouterr().out
    expectedPlateaInputInstructions = "Provide Plateau dimensions in the following format: maxCoordinateInX, maxCoordinateInY e.g : 5,5"
    assert printedOutput == expectedPlateaInputInstructions + "\n"


