from shutil import copy2
import os
import fileinput

def makeRender(latex):
    latexRenderDir = "render/{}/".format(latex.mainTitle)
    latexRenderFile = latexRenderDir + "{}.tex".format(latex.mainTitle)
    if not os.path.exists(latexRenderDir):
        os.makedirs(latexRenderDir)
    copy2('latexTemplate/template2.tex', latexRenderFile)

    replaceList = [["__NAME__", latex.author], ["__LITTLE_TITLE__", latex.subTitle], ["__MAIN_TITLE__", latex.mainTitle], ["__MAIN__", latex.finalMainData]]

    with open(latexRenderFile, "r") as infile:
        body = infile.read()
        for element in replaceList:
            body = body.replace(element[0], element[1])
    with open(latexRenderFile, "w") as outfile:
        outfile.write(body)
