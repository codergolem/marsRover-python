from src.rover import RoverPosition, Rover
from src.plateau import Plateau
from src.roverInstruction import RoverInstruction
from src.setOfInstructions import SetOfInstructions

class Parser:

    def parseFile(self, filePath):
        with open(filePath, 'r') as inputFile:
            plateauAsListOfStrings = inputFile.readline().split()
            plateau = Plateau(int(plateauAsListOfStrings[0]), int(plateauAsListOfStrings[1]))
            roverInstructions = []

            for lineCount, line in enumerate(inputFile, 1):
                if lineCount % 2 != 0:
                    roverInitialPositionAsList = line.split()
                    roverInitialPosition = RoverPosition(int(roverInitialPositionAsList[0]),
                                                         int(roverInitialPositionAsList[1]),
                                                         str(roverInitialPositionAsList[2]))
                else:
                    commandsToMoveRover = list(line)
                    roverInstruction = RoverInstruction(roverInitialPosition, commandsToMoveRover)
                    roverInstructions.append(roverInstruction)

        return SetOfInstructions(plateau, roverInstructions)
