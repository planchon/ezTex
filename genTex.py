#!/usr/bin/env python3

import sys
import os.path
import re

from genClass import *
from genInterpreter import *
from render import *

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

def findCodeEnd(data, index):
    for i in range(index, len(data)):
        if (data[i][0].lstrip().rstrip() == "END"):
            return i
    return -1

def findTabToDel(data):
    tabToDel = 1000
    for i in range(0, len(data)):
        tab = repr(data[i][0].count('\t'))
        print(tab > tabToDel)
        if (tab < tabToDel):
            tabToDel = tab
    return tabToDel


def processRawData(rawData):
    processedData = []
    inCode = False
    inCodeTabDel = 0
    index = 0
    for listOfData in rawData:
        tmpList = []
        for data in listOfData:
            if (data == '' or data[0] == '#'):
                pass
            elif (data.lstrip().rstrip() == "CODE"):
                    inCode = True
                    end = findCodeEnd(rawData, index)
                    inCodeTabDel = findTabToDel(rawData[index : end])
                    print inCodeTabDel
            else:
                tmp = data.lstrip().rstrip()
                tmpList.append(tmp)
        if len(tmpList) > 0:
            processedData.append(tmpList)
        index += 1
    return processedData

def main():
    fichier       = processConsoleArgs()
    rawData       = createRawData(fichier)
    processedData = processRawData(rawData)
    latexRawData  = interpretProcessedData(processedData)
    # latexRawData.processedChapter()
    # latexRawData.renderToLatex()
    # makeRender(latexRawData)


if __name__ == '__main__':
    main()
