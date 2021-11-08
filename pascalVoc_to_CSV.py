# coding: utf-8

import os
from lxml import etree
import csv

repertoireImages = "JPEGImages"
repertoireAnnotations = "annotations"
separateurOS = "/"
fichierOutput = "outPut.csv"

# classe représentant une box
class Box:
    def __init__(self, hash, label, xMin, yMin, xMax, yMax):
        self.m_hash = hash
        self.m_label = label
        self.m_xMin = xMin
        self.m_yMin = yMin
        self.m_xMax = xMax
        self.m_yMax = yMax

    def __str__(self):
        return self.m_hash + " " + self.m_label + " " + self.m_xMin + " " + self.m_yMin + " " + self.m_xMax + " " + self.m_yMax


# écriture sous forme csv
def ecriture(fichierDestination, listeBox):
    with open(fichierDestination, "w", newline="\n") as monFichier:
        writer = csv.writer(monFichier, delimiter=" ")
        for box in listeBox:
            writer.writerow([box.m_hash, box.m_label, box.m_xMin, box.m_yMin, box.m_xMax, box.m_yMax])


if __name__=="__main__":

    # recupérer la liste des images
    listeImage = os.listdir(repertoireImages)
    # liste des annotations à écrire dans le fichier csv
    listeBox = list()

    # pour chacune des images du dataSet
    compteur = 0
    for image in listeImage:
        # extraire le hash de l'image
        hash = image[0:len(image)-4]
        # retrouver le xml correspondant
        nomXml = hash + ".xml"
        # lecteur xml
        tree = etree.parse(repertoireAnnotations + separateurOS + nomXml)
        # pour chacune des boxs du xml, on créer un objet box la représentant et on l'ajoute à la liste
        for box in tree.xpath("/annotation/object"):
            boxChildren = box.getchildren()
            coordonneesBox = boxChildren[4]
            listeBox.append(Box(hash, boxChildren[0].text, coordonneesBox[0].text, coordonneesBox[1].text, coordonneesBox[2].text, coordonneesBox[3].text))
            #print(listeBox[-1])
        compteur += 1
    # écriture dans le fichier csv
    ecriture(fichierOutput, listeBox)
    print("Fin, ", compteur, " fichier xml ont été traitées")

