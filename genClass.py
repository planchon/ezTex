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

        def toStringData(self):
            finalString = ""
            for element in self.rawData:
                # print (len(element))
                for i in range(len(element)):
                    # print(element[i][0])
                    finalString += element[i][0]
            return finalString

class chapterObj(elementObj):

    def __init__(self, nameOfTheChapter):
        self.name = nameOfTheChapter

    def findEndObj(self, data, index):
        for i in range(index, len(data)):
            if data[i][0] == "END":
                return i
        print('No END sentence. Big ERROR. Stopping...')
        return -1000

    def findBreakPoint(self, data, index):
        breakpoints = ["ALGO", "CODE", "IMAGE", "END"]
        for i in range(index, len(data)):
            for brp in breakpoints:
                if data[i][0] == brp:
                    return i


    def processRawChapterData(self):
        i = 0
        end = 0
        dataList = self.rawData[0]
        print(self.name)
        self.processedData = []
        while i < len(dataList):
            data = dataList[i][0]
            # print(data)
            if data == "ALGO":
                end = self.findEndObj(dataList, i)
                print("ALGO", dataList[i : end])
                i = end + 1
            if data == "CODE":
                end = self.findEndObj(dataList, i)
                print("CODE", dataList[i : end])
                i = end + 1
            if data == "SUB_SECTION":
                end = self.findEndObj(dataList, i)
                print("SUB_SECTION", dataList[i : end])
                i = end + 1
            if data == "IMAGE":
                print("IMAGE", dataList[i])
                i = i + 1
            else:
                end = self.findBreakPoint(dataList, i)
                print("TEXT", dataList[i : end])
                if data == "END":
                    i = end + 1
                else:
                    i = end

                # BUG si i = end, comme a chaque fin de chapitre, on a un obj texte vide /!\

        print('-------')

class algoObj(elementObj):
    typeObj = "ALGO"
    pass

class codeObj(elementObj):
    typeObj = "CODE"
    pass

class imgObj(elementObj):
    typeObj = "IMAGE"
    pass

class textObj(elementObj):
    typeObj = "TEXT"
    pass
