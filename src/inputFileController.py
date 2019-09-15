from src.rover import RoverPosition, Rover


class InputFileController:

    rover: Rover

    def processFile(self, filePath):
        with open(filePath, 'rb') as inputFile:
            plateauAsListOfStrings = inputFile.readline().split()
            roverInitialPositionAsList = inputFile.readline().split()
            commandsToMoveRover = list(inputFile.readline())

        plateauCoordinateInX = int(plateauAsListOfStrings[0])
        plateauCoordinateInY = int(plateauAsListOfStrings[1])
        plateau = [plateauCoordinateInX, plateauCoordinateInY]

        roverInitialPosition = RoverPosition(int(roverInitialPositionAsList[0]),
                                             int(roverInitialPositionAsList[1]),
                                             str(roverInitialPositionAsList[2]))

        rover = Rover(plateau, roverInitialPosition)
        rover.processCommands(commandsToMoveRover)

        print(rover.getCurrentPosition().toString())