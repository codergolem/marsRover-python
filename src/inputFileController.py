from src.rover import Rover


class InputFileController:

    def __init__(self):
        self.rovers = []

    def processFile(self, filePath, parser):
        setOfInstructions = parser.parseFile(filePath)

        for instruction in setOfInstructions.getRoverInstructions():
            rover = Rover(setOfInstructions.plateau, instruction.getInitialPosition())
            rover.processCommands(instruction.getMovementCommands())
            print(rover.getCurrentPosition().toString())
