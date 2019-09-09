class CommandLineInput:

    plateauDimension = "Not Initialized"

    textToAskForPlateauDimension = "Provide Plateau dimension in this format: maxCoordinateX,maxCoordinateY e.g:5,5"
    textToAskForInitialPosition = "Provide Rover initial position:"
    textToAskForRoverMovementCommands = "Provide commands to move Rover:"

    roverInputInstructions = {}

    def startReceivingCommands(self):
        print(self.textToAskForPlateauDimension)
        plateauDimensionInRawFormat = input()
        print(self.textToAskForInitialPosition)
        initialPositionInRawFormat = input()
        print(self.textToAskForRoverMovementCommands)
        movementCommandInRawFormat = input()

        plateauDimensionInRoverFormat = plateauDimensionInRawFormat.split()
        initialPositionInRoverFormat  = initialPositionInRawFormat.split()

        rover = Rover(plateauDimensionInRawFormat,initialPositionInRawFormat)
        rover.move(movementCommandInRawFormat)
        print(rover.getCurrentPosition())

    def getPlateauDimension(self):
        return self.plateauDimension
