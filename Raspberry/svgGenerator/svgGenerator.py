#!/bin/python

import re
import svgwrite
import math

# Ratio utilisé pour les angles (pas/degres)
ratioAngle = 90/40
# Ratio utilisé pour les lignes (metres/pas)
ratioLigne = 10/2000 * 100

# Creation d'un fichier svg
dwg = svgwrite.Drawing('test.svg')

# Initialisation des variables
angle = 0
ligne = 0
xorg = 0
yorg = 0

# Ouverture d'un fichier d'input
with open("output", "r") as f :
    # Pour chaque ligne
    for line in f :
        # Si la ligne contient un angle
        if re.match("^A", line) is not None :
            # Trouver la valeur de l'angle en pas
            a = re.findall("([0-9]+)", line)
            # Transformer l'angle en degres
            a = int(a[0]) * ratioAngle

            # Ajoute l'angle à l'angle total
            angle += a

        # Si la ligne contient une distance
        elif re.match("^L", line) is not None :
            # Trouver la valeur de la distance en pas
            ligne = re.findall("([0-9]+)", line)
            # Transformer la ligne en metres
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

# Sauvegarde du fichier svg
dwg.save()
