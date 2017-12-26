def makeRender(latex):
    mainFinalString = ""
    for chapter in latex.chapter:
        for element in chapter.processedData:
            if element.typeObj == "ALGO":
                pass
            if element.typeObj == "TEXT":
                mainFinalString += "\n" + element.toStringData()
