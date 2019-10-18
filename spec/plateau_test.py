from marsrover.plateau import Plateau

class Test_Plateau:

    def test_shouldConvertToString(self):
        # Given
        plateau = Plateau(3, 3)
        exptectedPlateauAsString = '3 3'
        # When
        result = plateau.toString()
        assert exptectedPlateauAsString == result
