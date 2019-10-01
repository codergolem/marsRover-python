class RoverInstruction:

    def __init__(self, initialPosition, movementCommands):
        self.initialPosition = initialPosition
        self.movementCommands = movementCommands

    def getInitialPosition(self):
        return self.initialPosition

    def getMovementCommands(self):
        return self.movementCommands