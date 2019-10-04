class SetOfInstructions:

    def __init__(self, plateau, roverInstructions):
        self.plateau = plateau
        self.roverInstructions = roverInstructions

    def toString(self):
        plateauAsString = str(self.plateau.dimensionInX) + ' ' + str(self.plateau.dimensionInY) + '\n'
        roverInstructionsAsStrings = []
        for instruction in self.roverInstructions:
            movementCommandsAsString = ''.join([command.value for command in instruction.movementCommands])
            instructionAsString = instruction.initialPosition.toString() + '\n' + movementCommandsAsString
            roverInstructionsAsStrings.append(instructionAsString)
        return plateauAsString + '\n'.join(roverInstructionsAsStrings)
