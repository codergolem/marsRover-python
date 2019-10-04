from typing import List
from marsrover.position import RoverPosition
from marsrover.movementcommand import MovementCommand


class RoverInstruction:

    def __init__(self, initialPosition: RoverPosition, movementCommands: List[MovementCommand]):
        self.initialPosition: RoverPosition = initialPosition
        self.movementCommands: List[movementCommands] = movementCommands

