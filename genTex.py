import sys
import os.path
import re

from genClass import *
from genInterpreter import *

def processConsoleArgs():
    config = sys.argv[1:]
    if len(config) > 1:
        print('Veuillez passer le fichier gtex SEULEMENT')
        return 0
    fichier = sys.argv[1]
    if not os.path.exists(fichier):
        print('Ce fichier n\'existe pas')
        return 0
    else :
        return fichier

def createRawData(fichier):
    lines = []
    text = open(fichier)

    for line in text:
        tmpString = line.rstrip('\r\n').split("::")
        lines.append(tmpString)

    return lines

def processRawData(rawData):
    processedData = []
    for listOfData in rawData:
        tmpList = []
        for data in listOfData:
            if (data == '' or data[0] == '#'):
                pass
            else:
                tmp = data.lstrip().rstrip()
                tmpList.append(tmp)
        if len(tmpList) > 0:
            processedData.append(tmpList)

    return processedData

def main():
    fichier       = processConsoleArgs()
    rawData       = createRawData(fichier)
    processedData = processRawData(rawData)
    rawChapter    = interpretProcessedData(processedData)

if __name__ == '__main__':
    main()
