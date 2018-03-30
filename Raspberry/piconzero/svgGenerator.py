#!/bin/python

import re
import svgwrite
import math
import os
import sys

# Ratio utilisé pour les angles (pas/degres)
ratioAngle = 90/50
# Ratio utilisé pour les lignes (metres/pas)
ratioLigne = 2/132 * 10

if not os.path.exists(sys.argv[1]):
    os.makedirs(sys.argv[1])

# Creation d'un fichier svg
path = sys.argv[1] + "/" + sys.argv[2]
dwg = svgwrite.Drawing(path + '.svg', profile='tiny')

# Initialisation des variables
angle = 0
ligne = 0
xorg = 200
yorg = 20
perim = 0

# Ouverture d'un fichier d'input
with open("output_Perfect", "r") as f :
    # Pour chaque ligne
    for line in f :
        # Si la ligne contient un angle
        if re.match("^D", line) is not None :
            # Trouver la valeur de l'angle en pas
            a = re.findall("([0-9]+)", line)
            # Transformer l'angle en degres
            a = int(a[0]) * ratioAngle

            if(a>30):
                a = 90
                angle += a

        elif re.match("^G", line) is not None :
            # Trouver la valeur de l'angle en pas
            a = re.findall("([0-9]+)", line)
            # Transformer l'angle en degres
            a = int(a[0]) * ratioAngle

            # Toujours un angle droit
            if(a>30):
                a = 90
                angle -= a


        # Si la ligne contient une distance
        elif re.match("^L", line) is not None :
            # Trouver la valeur de la distance en pas
            ligne = re.findall("([0-9]+)", line)
            # Transformer la ligne en metres
            perim += int(ligne[0])
            ligne = int(ligne[0]) * ratioLigne
            print(ligne)

            # Calcul de la nouvelle position en utilisant socathoa
            x = xorg + math.sin(angle * math.pi/180) * ligne
            y = yorg + math.cos(angle * math.pi/180) * ligne
            print("x: " + str(x) + " y: " + str(y))

            # Ajout de la ligne allant de la dernière postion vers la nouvelle position au svg
            dwg.add(dwg.line((math.fabs(xorg), math.fabs(yorg)), (math.fabs(x), math.fabs(y)), stroke=svgwrite.rgb(10, 10, 16, '%')))

            # Enregistrement des anciennes valeurs
            xorg = x
            yorg = y

        else :
            # Si la ligne ne contient ni un angle ni une ligne on affiche une erreur
            print("Le fichier n'est pas correcte")
            exit()
    dwg.add(dwg.text(str(perim) + " pas", insert=(10, 20)))
    dwg.add(dwg.text(str(perim * ratioLigne/10) + " metres", insert=(10, 40)))



# Sauvegarde du fichier svg
dwg.save()
