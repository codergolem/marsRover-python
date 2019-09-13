from src.rover import RoverPosition
from mock import patch, mock_open
from src.inputFileController import InputFileController

class Test_InputFileController:

    def test_shouldCalculateFinalPositionForOneRover(self, mocker):
        # Given
        # inputFileController = InputFileController()
        filePath = 'somePathToFile/file.txt'
        mockedFileContent = '3 3\n2 2 N'
        expectedInitialPosition = RoverPosition(2, 2, "N")
        expectedPlateau = [3, 3]

        mockedRover = mocker.patch('src.rover.Rover', autospec=True)

        with patch('builtins.open', mock_open(read_data=mockedFileContent)):
            inputFileController = InputFileController()
            inputFileController.processFile(filePath)

        mockedRover.assert_called_with(expectedPlateau, expectedInitialPosition)
