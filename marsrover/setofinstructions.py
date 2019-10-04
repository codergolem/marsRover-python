from marsrover.instruction import RoverInstruction
from marsrover.plateau import Plateau
from typing import List


class SetOfInstructions:

    def __init__(self, plateau: Plateau, roverInstructions: List[RoverInstruction]):
        self.plateau: Plateau = plateau
        self.roverInstructions: List[RoverInstruction] = roverInstructions

    def toString(self) -> str:
        plateauAsString = str(self.plateau.dimensionInX) + ' ' + str(self.plateau.dimensionInY) + '\n'
        roverInstructionsAsStrings = []
        for instruction in self.roverInstructions:
            movementCommandsAsString = ''.join([command.value for command in instruction.movementCommands])
            instructionAsString = instruction.initialPosition.toString() + '\n' + movementCommandsAsString
            roverInstructionsAsStrings.append(instructionAsString)
        return plateauAsString + '\n'.join(roverInstructionsAsStrings)
