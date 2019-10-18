from marsrover.instruction import RoverInstruction
from marsrover.plateau import Plateau
from typing import List


class SetOfInstructions:

    def __init__(self, plateau: Plateau, roverInstructions: List[RoverInstruction]):
        self.plateau: Plateau = plateau
        self.roverInstructions: List[RoverInstruction] = roverInstructions

    def toString(self) -> str:
        roverInstructionsAsStrings = []
        for instruction in self.roverInstructions:
            roverInstructionsAsStrings.append(instruction.toString())
        return self.plateau.toString() + '\n' + '\n'.join(roverInstructionsAsStrings)
