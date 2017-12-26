class latexObj:
    mainTitle = ""
    subTitle  = ""
    author    = ""
    date      = ""
    # liste des obj text, algo, code, image
    chapter   = []

    def addChapter(self, chapterToAdd):
        self.chapter.append(chapterToAdd)

    def processedChapter(self):
        for element in self.chapter:
            element.processRawChapterData()

    def renderToLatex(self):
        pass

class elementObj:
        name = ""
        rawData = []
        processedData = []

        def __init__(self, name):
            self.name = name

        def __str__(self):
            if (len(self.processedData) > 0):
                return "\n" + self.name + " , processedData : " + str(self.processedData)
            else :
                return "\n" + self.name + " has no processedData, here is raw Data + \n" + str(self.rawData)

        def addRawData(self, data):
            self.rawData.append(data)

        def processRawData(self):
            pass

        def renderToLatex(self):
            pass

class chapterObj(elementObj):

    def __init__(self, nameOfTheChapter):
        self.name = nameOfTheChapter

    def processRawChapterData(self):
        data = self.rawData
        end = 0
        for i in range(len(data)):
            print(data[0][i][0])
            if data[i][0] == "ALGO":
                end = findEndObj(data, i)
                print(end)
            elif data[i][0] == "CODE":
                pass
            elif data[i][0] == "IMAGE":
                pass
            else :
                pass
                # c'est du texte.

    def findEndObj(data, index):
        for i in range(index, len(data)):
            if data[i] == "END":
                return i
        print('No END sentence. Big ERROR. Stopping...')
        return -1000

class algoObj(elementObj):
    pass
