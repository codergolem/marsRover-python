from marsrover.position import RoverPosition


class Plateau:

    def __init__(self, dimensionInX: int, dimensionInY: int):
        self.dimensionInX: int = dimensionInX
        self.dimensionInY: int = dimensionInY

    def isPositionWithinPlateauArea(self, position: RoverPosition):
        return not (position.coordinateInX > self.dimensionInX or
                position.coordinateInY > self.dimensionInY)
