class latexObj:
    mainTitle       = ""
    mainTitleHashed = ""
    subTitle        = ""
    author          = ""
    date            = ""
    finalMainData   = ""
    tableOfContent  = False
    preview         = False
    backup          = False
    save            = False
    chapter         = []
    images          = []

    def addChapter(self, chapterToAdd):
        self.chapter.append(chapterToAdd)

    def processedChapter(self):
        for element in self.chapter:
            element.processRawChapterData()

    def renderToLatex(self):
        if self.tableOfContent:
            self.finalMainData += "\\tableofcontents"
        for chapter in self.chapter:
            self.finalMainData += "\\section{" + chapter.name + "} \n"
            for objects in chapter.processedData:
                if objects.typeObj == "IMAGE":
                    self.images.append(objects.rawData[0][1])
                self.finalMainData += objects.renderToLatex()

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
        breakpoints = ["ALGO", "CODE", "IMAGE", "END", "SUB_SECTION", "SUB_SUB_SECTION"]
        for i in range(index, len(data)):
            for brp in breakpoints:
                if data[i][0] == brp:
                    return i

    def processRawChapterData(self):
        i = 0
        end = 0

        dataList = self.rawData[0]

        self.processedData = []

        print ('---------')

        while i < len(dataList):
            print ('managing', dataList[i])
            data = dataList[i][0]

            if data not in ["ALGO", "CODE", "IMAGE", "END", "SUB_SECTION","SUB_SUB_SECTION"]:
                data = "TEXT"

            print ('type ', data)
            # On traite chaque cas de breakpoint : image, code, algo...
            # et on les mets dans leur obj respectif en vue d'un traitement futur.

            if data == "ALGO":
                if len(dataList[i]) > 1:
                    algo = algoObj(dataList[i][1])
                else:
                    algo = algoObj("Algo sans titre")

                algo.rawData = []
                end = self.findEndObj(dataList, i)
                # print("ALGO", dataList[i : end])
                algo.addRawData(dataList[i : end])
                i = end
                self.processedData.append(algo)

            elif data == "CODE":

                if len(dataList[i]) > 1:
                    code = codeObj(dataList[i][1])
                else:
                    code = codeObj("code sans titre")

                code.rawData = []
                end = self.findEndObj(dataList, i)
                code.addRawData(dataList[i : end])
                i = end
                self.processedData.append(code)

            elif data == "SUB_SECTION":
                if len(dataList[i]) > 1:
                    sub = subSectionObj(dataList[i][1])
                else:
                    sub = subSectionObj("Sous section sans titre")

                # print("SUB_SECTION", dataList[i])
                sub.rawData = []
                sub.addRawData(dataList[i])
                i = i + 1
                self.processedData.append(sub)

            elif data == "SUB_SUB_SECTION":
                if len(dataList[i]) > 1:
                    sub = subsubSectionObj(dataList[i][1])
                else:
                    sub = subsubSectionObj("Sous section sans titre")

                # print("SUB_SECTION", dataList[i])
                sub.rawData = []
                sub.addRawData(dataList[i])
                i = i + 1
                self.processedData.append(sub)

            elif data == "IMAGE":
                if len(dataList[i]) > 1:
                    image = imgObj(dataList[i][1])
                    image.rawData = []
                    image.addRawData(dataList[i])
                else:
                    print("Une image a plus d'un argument. DSL D:")
                # print("IMAGE", dataList[i])
                i = i + 1
                self.processedData.append(image)

            elif data == "TEXT":
                # c'est du texte.
                text = textObj('Je suis du texte, j''ai pas de nom')
                end = self.findBreakPoint(dataList, i)
                # print ('break' , dataList[end])
                text.rawData = []
                if i != end:
                    text.addRawData(dataList[i : end])
                    print ('dataText', dataList[i : end])
                    self.processedData.append(text)
                    i = end
                else:
                    i += 1

            else :
                i += 1

            print ('>-- ')

class algoObj(elementObj):
    typeObj = "ALGO"

    def renderToLatex(self):
        return '\\texttt{YA UNE ALGO ICI} \\newline\\'

class codeObj(elementObj):
    typeObj = "CODE"

    def renderToLatex(self):
        finalString = ""
        data = self.rawData[0]
        lang = data[0][1]
        # print lang
        if (lang == "C++"):
            finalString += "\\begin{cppCode}{" + data[0][2] + "} \n"
            for i in range(1, len(data)):
                finalString += data[i][0] + "\n"
            finalString += "\\end{cppCode} \n"
        if (lang == "Java"):
            finalString += "\\begin{javaCode}{" + data[0][2] + "} \n"
            for i in range(1, len(data)):
                finalString += data[i][0] + "\n"
            finalString += "\\end{javaCode} \n"
        if (lang == "Tex"):
            finalString += "\\begin{texCode}{" + data[0][2] + "} \n"
            for i in range(1, len(data)):
                finalString += data[i][0] + "\n"
            finalString += "\\end{texCode} \n"
        if (lang == "bash"):
            finalString += "\\begin{bashCode}{" + data[0][2] + "} \n"
            for i in range(1, len(data)):
                finalString += data[i][0] + "\n"
            finalString += "\\end{bashCode} \n"

        return finalString

class imgObj(elementObj):
    typeObj = "IMAGE"
    pass

    def renderToLatex(self):
        finalString = ""
        finalString += "\\begin{figure}[h!] \n"
        finalString += "\\centerline{\\fbox{\\includegraphics[" + self.rawData[0][2] + "]{" + self.rawData[0][1] + "}}} \n"
        finalString += "\\caption{" + self.rawData[0][3] + "} \n"
        finalString += "\\end{figure}"
        return finalString

class subSectionObj(elementObj):
    typeObj = "SUB_SECTION"
    pass

    def renderToLatex(self):
        stringToLatex = ""
        stringToLatex = "\subsection{" + self.rawData[0][1] + "}"
        return stringToLatex

class subsubSectionObj(elementObj):
    typeObj = "SUB_SUB_SECTION"
    pass

    def renderToLatex(self):
        stringToLatex = ""
        stringToLatex = "\subsubsection{" + self.rawData[0][1] + "}"
        return stringToLatex

class textObj(elementObj):
    typeObj = "TEXT"

    def renderToLatex(self):
        stringToLatex = ""
        for element in self.rawData[0]:
            stringToLatex += element[0] + "\n"
        return stringToLatex
