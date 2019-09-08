import pytest

def test_canProvidePlateauDimensions(capsys):
    # Given
    commandLineInput = commandLineInput()
    # When
    commandLineInput.startReceivingCommands()

    # Then
    printedOutput = capsys.readouterr().out
    expectedPlateaInputInstructions = "Provide Plateau dimensions in the following format: maxCoordinateInX, maxCoordinateInY e.g : 5,5"
    assert printedOutput == expectedPlateaInputInstructions + "\n"


