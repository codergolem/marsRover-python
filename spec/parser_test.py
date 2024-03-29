from mock import patch, mock_open
from marsrover.parser import Parser
from marsrover.setofinstructions import SetOfInstructions
from marsrover.plateau import Plateau
from marsrover.instruction import RoverInstruction
from marsrover.position import RoverPosition
from marsrover.orientation import Orientation
from marsrover.movementcommand import MovementCommand
from marsrover.parsingerror import ParsingError
import pytest


class Test_Parser:

    def test_shouldParseAValidSetOfInstructions(self):
        # Given
        filePath = 'somePathToFile/file.txt'
        mockedFileContent = '5 5\n3 3 E\nMMR\n2 2 N\nRMLM'

        parser = Parser()

        plateau = Plateau(5, 5)
        movementCommands1 = [MovementCommand('M'), MovementCommand('M'), MovementCommand('R')]
        movementCommands2 = [MovementCommand('R'), MovementCommand('M'), MovementCommand('L'), MovementCommand('M')]
        roverInstruction1 = RoverInstruction(RoverPosition(3, 3, Orientation('E')), movementCommands1)
        roverInstruction2 = RoverInstruction(RoverPosition(2, 2, Orientation('N')), movementCommands2)

        expectedSetOfInstructions = SetOfInstructions(plateau, [roverInstruction1, roverInstruction2])

        # When
        with patch('builtins.open', mock_open(read_data=mockedFileContent)):
            result = parser.parseFile(filePath)

        # Then
        assert result.toString() == expectedSetOfInstructions.toString()

    def test_shouldRaiseExceptionWhenPlateauDimensionsAreNotValid(self):
        # Given
        filePath = 'somePathToFile/file.txt'
        mockedFileContent = 's 5\n3 3 E\nMMRMMRMRRM'

        parser = Parser()

        # Then
        with pytest.raises(ParsingError, match='Invalid plateau dimensions'):
            with patch('builtins.open', mock_open(read_data=mockedFileContent)):
                parser.parseFile(filePath)

    def test_shouldRaiseExceptionWhenPlateauDimensionsAreNotExactlyTwo(self):
        # Given
        filePath = 'somePathToFile/file.txt'
        mockedFileContent = 'hjhkjj\n3 3 E\nMMRMMRMRRM'

        parser = Parser()

        # Then
        with pytest.raises(ParsingError, match='Invalid plateau dimensions'):
            with patch('builtins.open', mock_open(read_data=mockedFileContent)):
                parser.parseFile(filePath)

    def test_shouldRaiseExceptionWhenInitialPositionIsNotValid(self, capsys):
        # Given
        filePath = 'somePathToFile/file.txt'
        mockedFileContent = '5 5\n3 s E\nMMRMMRMRRM\n2 2 N\nMRMLM\n1 1 N\nM'

        parser = Parser()

        # Then
        with pytest.raises(ParsingError, match='Invalid rover initial position'):
            with patch('builtins.open', mock_open(read_data=mockedFileContent)):
                parser.parseFile(filePath)

    def test_shouldRaiseExceptionWhenInitialPositionIsNotExactlyThreeValues(self, capsys):
        # Given
        filePath = 'somePathToFile/file.txt'
        mockedFileContent = '5 5\n3 3\nMMRMMRMRRM\n2 2 N\nMRMLM\n1 1 N\nM'

        parser = Parser()

        # Then
        with pytest.raises(ParsingError, match='Invalid rover initial position'):
            with patch('builtins.open', mock_open(read_data=mockedFileContent)):
                parser.parseFile(filePath)

    def test_shouldRaiseExceptionIfPlateauDimensionsAreNotExactlyTwo(self):
        # Given
        filePath = 'somePathToFile/file.txt'
        mockedFileContent = '5\n3 3 E\nMMRMMRMRRM'

        parser = Parser()

        # Then
        with pytest.raises(ParsingError, match='Invalid plateau dimensions'):
            with patch('builtins.open', mock_open(read_data=mockedFileContent)):
                parser.parseFile(filePath)

    def test_shouldRaiseExceptionWhenInitialOrientationIsNotValid(self, capsys):
        # Given
        filePath = 'somePathToFile/file.txt'
        mockedFileContent = '5 5\n3 3 X\nMMRMMRMRRM\n2 2 N\nMRMLM\n1 1 N\nM'

        parser = Parser()

        # Then
        with pytest.raises(ParsingError, match="Invalid rover initial position"):
            with patch('builtins.open', mock_open(read_data=mockedFileContent)):
                parser.parseFile(filePath)

    def test_shouldRaiseExceptionWhenAnMovementCommandIsNotValid(self, capsys):
        # Given
        filePath = 'somePathToFile/file.txt'
        mockedFileContent = '5 5\n3 3 E\nMMRXMRMRRM\n2 2 N\nMRMLM\n1 1 N\nM'
        parser = Parser()

        # Then
        with pytest.raises(ValueError, match="'X' is not a valid MovementCommand"):
            with patch('builtins.open', mock_open(read_data=mockedFileContent)):
                parser.parseFile(filePath)
