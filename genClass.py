class latexObj:
    mainTitle = ""
    subTitle  = ""
    author    = ""
    date      = ""
    # liste des obj text, algo, code, image
    chapter   = []

    def addChapter(self, chapterToAdd):
        self.chapter.append(chapterToAdd)


class elementObj:
        name = ""
        rawData = []
        processedData = []

        def __init__(self, name):
            self.name = name

        def __str__(self):
            if (len(processedData) > 0):
                return name + " , processedData : " + str(processedData)
            else :
                return name + " has no processedData, here is raw Data + \n" + str(rawData)

        def addRawData(self, data):
            self.rawData.append(data)

        def processRawData(self):
            pass

        def renderToLatex(self):
            pass

class chapterObj(elementObj):
    def __init__(self, nameOfTheChapter):
        self.chapterName = nameOfTheChapter
        print ('Chapter : "' + nameOfTheChapter + '" initialized.')

    def processRawChapterData(data):
        for i in range(leng(data)):
            if data[i][0] == "ALGO":
                pass
            elif data[i][0] == "CODE":
                pass
            elif data[i][0] == "IMAGE":
                pass
            else :
                pass
                # c'est du texte.

class algoObj(elementObj):
    pass
