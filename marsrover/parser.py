from marsrover.rover import RoverPosition, Rover
from marsrover.plateau import Plateau
from marsrover.instruction import RoverInstruction
from marsrover.setofinstructions import SetOfInstructions
from marsrover.orientation import Orientation
from marsrover.parsingerror import ParsingError
from marsrover.movementcommand import MovementCommand


class Parser:

    def parseFile(self, filePath):
        with open(filePath, 'r') as inputFile:
            plateauAsListOfStrings = inputFile.readline().split()
            if not ((len(plateauAsListOfStrings) == 2) and
                    str.isdigit(plateauAsListOfStrings[0]) and
                    str.isdigit(plateauAsListOfStrings[1])):
                raise ParsingError("Invalid plateau dimensions")

            plateau = Plateau(int(plateauAsListOfStrings[0]), int(plateauAsListOfStrings[1]))
            roverInstructions = []

            for lineCount, line in enumerate(inputFile, 1):
                if lineCount % 2 != 0:
                    roverInitialPositionAsList = line.split()
                    if not ((len(roverInitialPositionAsList) == 3) and
                            str.isdigit(roverInitialPositionAsList[0]) and
                            str.isdigit(roverInitialPositionAsList[1])):
                        raise ParsingError("Invalid rover initial position")

                    orientation = Orientation(roverInitialPositionAsList[2])

                    roverInitialPosition = RoverPosition(int(roverInitialPositionAsList[0]),
                                                         int(roverInitialPositionAsList[1]),
                                                         orientation)
                else:
                    commandsToMoveRover = [MovementCommand(command) for command in list(line.replace('\n', ''))]
                    roverInstruction = RoverInstruction(roverInitialPosition, commandsToMoveRover)
                    roverInstructions.append(roverInstruction)

        return SetOfInstructions(plateau, roverInstructions)
