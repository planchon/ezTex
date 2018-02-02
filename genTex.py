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
        tab = int(repr(data[i][0].count('\t')))
        if (tab < tabToDel):
            tabToDel = tab
    return tabToDel


def processRawData(rawData):

    processedData = []
    end = 0
    index = 0
    tabToDel = 0
    areInCode = False
    # processedData est une liste des datas :
    # CODE, LANG, TITRE : CODE
    # ALGO, TITRE : ALGO...


    for i in range(len(rawData)):
        if rawData[i][0] == '' or rawData[i][0][0] == '#':
            pass
        else:
            if rawData[i][0].rstrip().lstrip() == "CODE":
                areInCode = True
                if rawData[i][2] != '':
                    processedData.append(['CODE', rawData[i][1].rstrip().lstrip(), rawData[i][2].rstrip().lstrip()])
                else:
                    processedData.append(['CODE', rawData[i][1].rstrip().lstrip(), ''])
                end = findCodeEnd(rawData, i)
                tabToDel = findTabToDel(rawData[i : end])
                for ii in range(i + 1, end): #[i+1, i+1 + 1, i+1 + 2, ..., end]
                    processedData.append([rawData[ii][0][tabToDel * 2:].rstrip()])
            elif rawData[i][0].rstrip().lstrip() == "END" and areInCode:
                areInCode = False
                processedData.append(['END'])
            else:
                listTemp = []
                if not areInCode:
                    for element in rawData[i]:
                            listTemp.append(element.lstrip().rstrip())
                    print listTemp
                    processedData.append(listTemp)

    return processedData

def main():
    fichier       = processConsoleArgs()
    rawData       = createRawData(fichier)
    processedData = processRawData(rawData)
    latexRawData  = interpretProcessedData(processedData)
    latexRawData.processedChapter()
    latexRawData.renderToLatex()
    makeRender(latexRawData)


if __name__ == '__main__':
    main()
