from marsrover.rover import RoverPosition, Rover
from marsrover.plateau import Plateau
from marsrover.instruction import RoverInstruction
from marsrover.setofinstructions import SetOfInstructions
from marsrover.orientation import Orientation
from marsrover.parsingerror import ParsingError
from marsrover.movementcommand import MovementCommand
from typing import List
import re


class Parser:

    validPlateauInput = re.compile("^[0-9]* [0-9]*$")
    validRoverPosition = re.compile("^[0-9]* [0-9]* [NSEW]$")

    def parseFile(self, filePath: str) -> SetOfInstructions:
        with open(filePath, 'r') as inputFile:
            plateauInputLine = inputFile.readline()
            plateau = self.parsePlateauInput(plateauInputLine)

            roverInstructions = []
            for lineCount, line in enumerate(inputFile, 1):
                if lineCount % 2 != 0:
                    roverInitialPosition = self.parseInitialPosition(line)
                else:
                    roverInstruction = RoverInstruction(roverInitialPosition, self.parseMovementCommands(line))
                    roverInstructions.append(roverInstruction)

        return SetOfInstructions(plateau, roverInstructions)

    def parseMovementCommands(self, line: str) -> List[MovementCommand]:
        commandsToMoveRover = [MovementCommand(command) for command in list(line.replace('\n', ''))]
        return commandsToMoveRover

    def parseInitialPosition(self, line: str) -> RoverPosition:
        if not re.match(self.validRoverPosition, line):
            raise ParsingError("Invalid rover initial position")
        inputLineAsList = line.split()
        orientation = Orientation(inputLineAsList[2])
        return RoverPosition(int(inputLineAsList[0]),
                             int(inputLineAsList[1]),
                             orientation)

    def parsePlateauInput(self, inputString: str) -> Plateau:
        if not re.match(self.validPlateauInput, inputString):
            raise ParsingError("Invalid plateau dimensions")
        inputStringAsList = inputString.split()
        return Plateau(int(inputStringAsList[0]), int(inputStringAsList[1]))
