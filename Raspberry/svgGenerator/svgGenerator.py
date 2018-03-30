#!/usr/bin/python

import re
import svgwrite
import math
import os
import sys

ratioAngle = 90/50
ratioLigne = 2/132 * 10

if not os.path.exists(sys.argv[1]):
    os.makedirs(sys.argv[1])

path = sys.argv[1] + "/" + sys.argv[2]
dwg = svgwrite.Drawing(path + '.svg', profile='tiny')

angle = 0
ligne = 0
xorg = 200
yorg = 20
perim = 0
a = False

with open("output", "r") as f :
    for line in f :
        if re.match("^D", line) is not None :
            a = re.findall("([0-9]+)", line)
            a = int(a[0]) * ratioAngle

            if(a>30):
                a = 90
                angle += a

        elif re.match("^G", line) is not None :
            a = re.findall("([0-9]+)", line)
            a = int(a[0]) * ratioAngle

            if(a>30):
                a = 90
                angle -= a


        elif re.match("^L", line) is not None :
            if(a == False):
                a = True
            else:
                ligne = re.findall("([0-9]+)", line)
                perim += int(ligne[0])
                ligne = int(ligne[0]) * ratioLigne
                print(ligne)

                x = xorg + math.sin(angle * math.pi/180) * ligne
                y = yorg + math.cos(angle * math.pi/180) * ligne
                print("x: " + str(x) + " y: " + str(y))

                dwg.add(dwg.line((math.fabs(xorg), math.fabs(yorg)), (math.fabs(x), math.fabs(y)), stroke=svgwrite.rgb(10, 10, 16, '%')))

                xorg = x
                yorg = y

        else :
            print("Le fichier n'est pas correcte")
            exit()
    dwg.add(dwg.text(str(perim) + " pas", insert=(10, 20)))
    dwg.add(dwg.text(str(perim * ratioLigne/10) + " metres", insert=(10, 40)))



dwg.save()
