class SetOfInstructions:

    def __init__(self, plateau, roverInstructions):
        self.plateau = plateau
        self.roverInstructions = roverInstructions

    def getPlateau(self):
        return self.plateau

    def getRoverInstructions(self):
        return self.roverInstructions

    def toString(self):
        plateauAsString = str(self.plateau.getDimensionInX()) + ' ' + str(self.plateau.getDimensionInY()) + '\n'
        roverInstructionsAsStrings = []
        for instruction in self.roverInstructions:
            movementCommandsAsString = ''.join([command.value for command in instruction.getMovementCommands()])
            instructionAsString = instruction.getInitialPosition().toString() + '\n' + movementCommandsAsString
            roverInstructionsAsStrings.append(instructionAsString)
        return plateauAsString + '\n'.join(roverInstructionsAsStrings)
