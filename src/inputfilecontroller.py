from src.rover import Rover
from src.parsingerror import ParsingError


class InputFileController:

    def __init__(self):
        self.rovers = []

    def processFile(self, filePath, parser):
        try:
            setOfInstructions = parser.parseFile(filePath)
            for instruction in setOfInstructions.getRoverInstructions():
                rover = Rover(setOfInstructions.plateau, instruction.getInitialPosition())
                rover.processCommands(instruction.getMovementCommands())
                print(rover.getCurrentPosition().toString())
        except ParsingError as error:
            print(error)
        except ValueError as error:
            print(error)
