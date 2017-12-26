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
        data = self.rawData[0]
        end = 0
        self.processedData = []
        for i in range(len(data)):
            if data[i][0] == "ALGO":
                if(len(data[i]) == 1):
                    algo = algoObj("Algo sans titre")
                else :
                    algo = algoObj(data[i][0])
                algo.rawData = []
                end = self.findEndObj(data, i)
                algo.addRawData(data[i : end])
                self.processedData.append(algo)
                i += end
            elif data[i][0] == "CODE":
                if(len(data[i]) == 1):
                    code = codeObj("Code sans titre")
                else :
                    code = codeObj(data[i][0])
                code.rawData = []
                end = self.findEndObj(data, i)
                code.addRawData(data[i : end])
                self.processedData.append(code)
                i += end
            elif data[i][0] == "IMAGE":
                pass
            else :
                text = textObj("")
                text.rawData = []
                end = self.findBreakPoint(data, i)
                if(data[i : end] != []):
                    text.addRawData(data[i : end])
                    print (data[i : end])
                    self.processedData.append(text)
                i += end


                # ATTENTION IL Y A UN BUG : 
                # le dernier element de cahque text va au debut du precedent...
                # wtf

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
