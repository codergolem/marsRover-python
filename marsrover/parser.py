from marsrover.rover import RoverPosition, Rover
from marsrover.plateau import Plateau
from marsrover.instruction import RoverInstruction
from marsrover.setofinstructions import SetOfInstructions
from marsrover.orientation import Orientation
from marsrover.parsingerror import ParsingError
from marsrover.movementcommand import MovementCommand
import re


class Parser:

    validPlateauInput = re.compile("^[0-9]* [0-9]*$")
    validRoverPosition = re.compile("^[0-9]* [0-9]* [NSEW]$")

    def parseFile(self, filePath: str) -> SetOfInstructions:
        with open(filePath, 'r') as inputFile:
            plateauInputLine = inputFile.readline()
            if not re.match(self.validPlateauInput, plateauInputLine):
                raise ParsingError("Invalid plateau dimensions")
            plateau = Plateau(int(plateauInputLine.split()[0]), int(plateauInputLine.split()[1]))

            roverInstructions = []
            for lineCount, line in enumerate(inputFile, 1):
                if lineCount % 2 != 0:
                    if not re.match(self.validRoverPosition, line):
                        raise ParsingError("Invalid rover initial position")
                    orientation = Orientation(line.split()[2])
                    roverInitialPosition = RoverPosition(int(line.split()[0]),
                                                         int(line.split()[1]),
                                                         orientation)
                else:
                    commandsToMoveRover = [MovementCommand(command) for command in list(line.replace('\n', ''))]
                    roverInstruction = RoverInstruction(roverInitialPosition, commandsToMoveRover)
                    roverInstructions.append(roverInstruction)

        return SetOfInstructions(plateau, roverInstructions)
