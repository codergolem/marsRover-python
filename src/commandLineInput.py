class CommandLineInput:
    plateauDimension = "Not Initialized"
    plateauDimensionInputInstruction = "Provide Plateau dimension in this format: maxCoordinateX,maxCoordinateY e.g:5,5"

    def startReceivingCommands(self):
        print(self.plateauDimensionInputInstruction)
        self.plateauDimension = input()

    def getPlateauDimension(self):
        return self.plateauDimension
