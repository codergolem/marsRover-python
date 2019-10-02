from src.rover import RoverPosition, Rover
from src.plateau import Plateau
from src.roverInstruction import RoverInstruction
from src.setOfInstructions import SetOfInstructions
from src.orientation import Orientation
from src.ParsingError import ParsingError


class Parser:
    # TODO: Make movement command a ENUM and handle exception
    # TODO: Handle exception if orientation is not one of the valid enums

    def parseFile(self, filePath):
        with open(filePath, 'r') as inputFile:
            plateauAsListOfStrings = inputFile.readline().split()
            if not (str.isdigit(plateauAsListOfStrings[0]) and str.isdigit(plateauAsListOfStrings[1])):
                raise ParsingError("Invalid plateau dimensions")

            plateau = Plateau(int(plateauAsListOfStrings[0]), int(plateauAsListOfStrings[1]))
            roverInstructions = []

            for lineCount, line in enumerate(inputFile, 1):
                if lineCount % 2 != 0:
                    roverInitialPositionAsList = line.split()
                    orientation = Orientation(roverInitialPositionAsList[2])
                    if not (str.isdigit(roverInitialPositionAsList[0]) and str.isdigit(roverInitialPositionAsList[1])):
                        raise ParsingError("Invalid rover initial position")

                    roverInitialPosition = RoverPosition(int(roverInitialPositionAsList[0]),
                                                         int(roverInitialPositionAsList[1]),
                                                         orientation)
                else:
                    commandsToMoveRover = list(line)
                    roverInstruction = RoverInstruction(roverInitialPosition, commandsToMoveRover)
                    roverInstructions.append(roverInstruction)

        return SetOfInstructions(plateau, roverInstructions)
