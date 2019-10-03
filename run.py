from marsrover.inputfilecontroller import InputFileController
from marsrover.parser import Parser


def main():
    parser = Parser()
    inputFileController = InputFileController()
    inputFile = 'inputFile.txt'
    inputFileController.processFile(inputFile, parser)


if __name__ == '__main__':
    main()
