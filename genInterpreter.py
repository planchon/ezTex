from genClass import *

def interpretProcessedData(processedData):
    index = 0
    latex = latexObj()
    for lines in processedData:
        dataToChapter = []
        if lines[0] == "TITLE":
            latex.mainTitle = lines[1]
        if lines[0] == "SUB_TITLE":
            latex.subTitle = lines[1]
        if lines[0] == "AUTHOR":
            latex.author = lines[1]
        if lines[0] == "DATE":
            latex.date = lines[1]
        if lines[0] == "TABLE_OF_CONTENT" and lines[1] == "TRUE":
            latex.tableOfContent = True
        if lines[0] == "PREVIEW" and lines[1] == "TRUE":
            latex.preview = True
        if lines[0] == "BACK_UP" and lines[1] == "TRUE":
            latex.backup = True
        if lines[0] == "CHAPTER":
            chapter = chapterObj(lines[1])
            chapter.rawData = []
            endOfChapter = findEndChapter(processedData, index)
            dataToChapter = processedData[index + 1 : endOfChapter]
            print dataToChapter
            chapter.addRawData(dataToChapter)
            latex.addChapter(chapter)
        index += 1
    return latex

def findEndChapter(data, index):
    for i in range(index, len(data)):
        if i+1 < len(data):
            if ((data[i][0] == "END") and (data[i+1][0] == "CHAPTER")):
                return i+1
        else :
            if(data[i][0] == "END"):
                return i+1

    print('Chapter END not found. Error in your file')
    return -1000
