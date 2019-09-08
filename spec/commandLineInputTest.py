import pytest
import sys
import builtins

from src.commandLineInput import CommandLineInput

def test_canProvidePlateauDimensions(capsys):
    # Given
    commandLineInput = CommandLineInput()
    samplePlateauDimension = "5,5"
    # When
    builtins.input = lambda: samplePlateauDimension
    commandLineInput.startReceivingCommands()
    printedOutput = capsys.readouterr().out
    # Then
    expectedPlateauInputInstructions = "Provide Plateau dimension in this format: maxCoordinateX,maxCoordinateY e.g:5,5"
    assert printedOutput == expectedPlateauInputInstructions + "\n"
    assert commandLineInput.getPlateauDimension() == samplePlateauDimension

