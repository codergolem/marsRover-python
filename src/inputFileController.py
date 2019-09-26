from src.rover import RoverPosition, Rover


class InputFileController:

    def __init__(self):
        self.rovers = []

    def processFile(self, filePath):
        with open(filePath, 'r') as inputFile:
            plateauAsListOfStrings = inputFile.readline().split()
            plateauCoordinateInX = int(plateauAsListOfStrings[0])
            plateauCoordinateInY = int(plateauAsListOfStrings[1])
            plateau = [plateauCoordinateInX, plateauCoordinateInY]

            for lineCount, line in enumerate(inputFile, 1):
                if lineCount % 2 != 0:
                    roverInitialPositionAsList = line.split()
                    roverInitialPosition = RoverPosition(int(roverInitialPositionAsList[0]),
                                                         int(roverInitialPositionAsList[1]),
                                                         str(roverInitialPositionAsList[2]))
                else:
                    commandsToMoveRover = list(line)
                    rover = Rover(plateau, roverInitialPosition)
                    rover.processCommands(commandsToMoveRover)
                    self.rovers.append(rover)

        for rover in self.rovers:
            print(rover.getCurrentPosition().toString())
