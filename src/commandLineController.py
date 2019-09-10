from src.rover import Rover


class CommandLineController:

    textToAskForPlateauDimension = "Provide Plateau dimension in this format: maxCoordinateX,maxCoordinateY e.g:5,5"
    textToAskForInitialPosition = "Provide Rover initial position:"
    textToAskForRoverMovementCommands = "Provide commands to move Rover:"

    # TODO: Validate user input
    def startReceivingCommands(self):
        print(self.textToAskForPlateauDimension)
        plateauDimension = input().split()
        plateauCoordinateInX = int(plateauDimension[0])
        plateauCoordinateInY = int(plateauDimension[1])
        plateauDimension = [plateauCoordinateInX, plateauCoordinateInY]
        print(self.textToAskForInitialPosition)
        initialPosition = input().split()
        initialCoordinateInX = int(initialPosition[0])
        initialCoordinateInY = int(initialPosition[1])
        initialOrientation = initialPosition[2]
        initialPosition = [initialCoordinateInX, initialCoordinateInY, initialOrientation]
        print(self.textToAskForRoverMovementCommands)
        movementCommands = list(input())
        # TODO: Test that the valuerror exception corresponds to the actual invalid input
        try:
            rover = Rover(plateauDimension, initialPosition)
            rover.processCommands(movementCommands)
            print("Final Position: " + rover.getCurrentPosition().toString())
        except ValueError:
            print('invalid input: rover out of plateau area')
