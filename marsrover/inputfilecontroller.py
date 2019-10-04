from marsrover.rover import Rover
from marsrover.parsingerror import ParsingError


class InputFileController:

    def __init__(self):
        self.rovers = []

    def processFile(self, filePath, parser):
        try:
            setOfInstructions = parser.parseFile(filePath)
            for instruction in setOfInstructions.roverInstructions:
                rover = Rover(setOfInstructions.plateau, instruction.initialPosition)
                rover.processCommands(instruction.movementCommands)
                print(rover.currentPosition.toString())
        except ParsingError as error:
            print(error)
        except ValueError as error:
            print(error)
