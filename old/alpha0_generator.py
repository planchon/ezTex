import sys
import os.path


class ChapterClass:
    objects = []
    def __init__(self, title):
        self.title = title

    def __str__(self):
        finalString = ""
        for items in self.objects:
            finalString += "NEW OBJ\n"
            finalString += "," + items.__str__()
        return finalString

    def addObject(self, newObjects):
        self.objects.append(newObjects)

class textObj:
    textListe = []

    def __init__(self):
        pass

    def __str__(self):
        finalString = ""
        for items in self.textListe:
            finalString += " -- NEW TEXT :\n"
            finalString += items + "\n"
        return finalString

    def addText(self, text):
        self.textListe.append(text)

class algoObj:
    rawInput    = []
    finalOutput = []

    def addData(self, data):
        self.rawInput.append(data)

    def processInput(input):
        pass

class imgObj:
    imgLink    = ""
    imgCaption = ""
    imgSize    = ""

    def processInput(input):
        pass

class codeObj:
    rawInput = []
    finalOutput = []

    def addData(self, data):
        self.rawInput.append(data)

    def processInput(input):
        pass

CONFIG = {
    "little title" : "little_title",
    "main title"   : "main_title",
    "author"       : "author",
    "chapter"      : []
}

def openTemplateFile():
    config = sys.argv[1:]
    if len(config) > 1:
        print('Veuillez passer le fichier ptex SEULEMENT')
        return 0
    fichier = sys.argv[1]
    if not os.path.exists(fichier):
        print('Ce fichier n\'existe pas')
        return 0
    else :
        print('Le fichier existe. Tout est ok :D')
        return fichier

def parseFile(fichier):
    lines = []
    text = open(fichier)
    for line in text:
        lines.append(line.rstrip('\r\n').split(' : '))
    return lines

def parseChapter(lines, title):
    chapter = ChapterClass(title)
    requestNewTextObj = False
    text = textObj()
    for i in range(0, len(lines)):
        firstWord = lines[i][0]
        if   (firstWord == "CODE"):
            print("CODE")
            chapter.addObject(text)
            text = textObj()
            closestEnd = findClosestEnd(lines, "END", i)
            code = codeObj()
            code.addData(lines[i + 1 : closestEnd - 1])
            chapter.addObject(code)
        elif (firstWord == "ALGO"):
            print("ALGO")
            chapter.addObject(text)
            text = textObj()
            closestEnd = findClosestEnd(lines, "END", i)
            algo = algoObj()
            algo.addData(lines[i + 1 : closestEnd - 1])
            chapter.addObject(algo)
        elif (firstWord == "IMAGE"):
            print("IMAGE")
            chapter.addObject(text)
            text = textObj()
            closestEnd = findClosestEnd(lines, "END", i)
            pass
        else:
            print("WORD")
            text.addText(lines[i])
    return chapter

def findClosestEnd(array, word, index):
    for i in range(index, len(array)):
        for args in array[i]:
            if args == word:
                return index
            index += 1
    print ("PAS DE FIN -> ERREUR !")
    return 0

def parserLines(lines):
    index = 0
    for line in lines:
        for args in line:
            if args == "LITTLE_TITLE":
                CONFIG["little title"] = line[1]
            if args == "MAIN_TITLE":
                CONFIG["main title"] = line[1]
            if args == "AUTHOR":
                CONFIG["author"] = line[1]
            if args == "CHAPTER":
                indexEnd = findClosestEnd(lines, "END", index)
                linesToParser = lines[index + 1 : indexEnd - 1]
                CONFIG["chapter"].append(parseChapter(linesToParser, lines[index][1]))
        index += 1

if __name__ == '__main__':
    fichier = openTemplateFile()
    lines   = parseFile(fichier)
    parserLines(lines)
    # print(CONFIG["chapter"][1])
