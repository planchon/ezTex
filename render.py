from shutil import copy2
import os
import fileinput
import hashlib

def makeRender(latex):
    hashName = hashlib.md5(latex.mainTitle)
    latex.mainTitleHashed = hashName.hexdigest()
    latexRenderDir = ".tmp/{}/".format(latex.mainTitleHashed)
    latexRenderFilePDF = latexRenderDir + "{}.pdf".format(latex.mainTitleHashed)
    latexRenderFile = latexRenderDir + "{}.tex".format(latex.mainTitleHashed)
    if not os.path.exists(latexRenderDir):
        os.makedirs(latexRenderDir)
    copy2('latexTemplate/template.tex', latexRenderFile)
    copy2('latexTemplate/logo.png', latexRenderDir + "/logo.png")
    copy2('latexTemplate/mcode.sty', latexRenderDir + "/mcode.sty")

    replaceList = [["__NAME__", latex.author], ["__LITTLE_TITLE__", latex.subTitle], ["__MAIN_TITLE__", latex.mainTitle], ["__MAIN__", latex.finalMainData]]

    with open(latexRenderFile, "r") as infile:
        body = infile.read()
        for element in replaceList:
            body = body.replace(element[0], element[1])
    with open(latexRenderFile, "w") as outfile:
        outfile.write(body)

    os.chdir(latexRenderDir)
    command = "pdflatex " + latex.mainTitleHashed + ".tex"

    for i in range(3):
        os.system(command)

    if (latex.preview):
        command = "evince " + latex.mainTitleHashed + ".pdf"
        os.system(command)

    os.chdir("../..")

    copy2(latexRenderFilePDF, 'render/{}'.format(latex.mainTitle + ".pdf"))
    os.system("clear")

    print("La PDF a ete sauvgarder comme " + latex.mainTitle + ".pdf dans /render \n Merci d\'avoir utilise genTex !")
