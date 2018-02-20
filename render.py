from shutil import copy2
import os
import fileinput
import hashlib
import sys
import datetime

def makeRender(latex):

    now = datetime.datetime.now()

    hashName = hashlib.md5(latex.mainTitle)
    if latex.backup:
        latex.mainTitleHashed = hashName.hexdigest() + '_' + now.strftime("%d-%m-%Y_%H:%M")
    else:
        latex.mainTitleHashed = hashName.hexdigest()
    latexRenderDir = ".tmp/{}/".format(latex.mainTitleHashed)
    latexRenderFilePDF = latexRenderDir + "{}.pdf".format(latex.mainTitleHashed)
    latexRenderFile = latexRenderDir + "{}.tex".format(latex.mainTitleHashed)
    if not os.path.exists(latexRenderDir):
        os.makedirs(latexRenderDir)

    for image in latex.images:
        if not os.path.exists(((sys.argv[1]).split('/'))[0] + '/' + image):
            print ('L\'image ' + image + ' n\'est pas dans le dossier du fichier ezTex. FIN' )
            return
        else:
            copy2(((sys.argv[1]).split('/'))[0] + '/' + image, latexRenderDir)

    copy2('latexTemplate/template.tex', latexRenderFile)
    copy2('latexTemplate/logo.png', latexRenderDir + "/logo.png")

    replaceList = [["__NAME__", latex.author], ["__LITTLE_TITLE__", latex.subTitle], ["__MAIN_TITLE__", latex.mainTitle], ["__MAIN__", latex.finalMainData]]

    with open(latexRenderFile, "r") as infile:
        body = infile.read()
        for element in replaceList:
            body = body.replace(element[0], element[1])
    with open(latexRenderFile, "w") as outfile:
        outfile.write(body)

    os.chdir(latexRenderDir)
    command = "pdflatex " + latex.mainTitleHashed + ".tex"

    for i in range(2):
        os.system(command)

    if (latex.preview):
        command = "evince " + latex.mainTitleHashed + ".pdf"
        os.system(command)

    os.chdir("../..")

    if latex.save:
        copy2(latexRenderFilePDF, 'render/{}'.format(latex.mainTitle + ".pdf"))
        os.system("clear")
        print("La PDF a ete sauvgarder comme " + latex.mainTitle + ".pdf dans /render \n Merci d\'avoir utilise genTex !")
