#!/bin/python

import re
import svgwrite
import math

ratio = 90/40

dwg = svgwrite.Drawing('test.svg')
angle = 0
A = 0
ligne = 0
xorg = 0
yorg = 0

with open("exemple", "r") as f :
    for line in f :
        if re.match("^A", line) is not None :
            angle = re.findall("([0-9]+)", line)
            angle = int(angle[0]) * ratio
            print("Angle : ", angle)
            A += angle

        elif re.match("^L", line) is not None :
            ligne = re.findall("([0-9]+)", line)
            ligne = int(ligne[0])
            print("Line : ", ligne)

            x = xorg + math.sin(A * math.pi/180) * int(ligne) #socathoa
            y = yorg + math.cos(A * math.pi/180) * int(ligne) #socathoa
            print("x: ",x)
            print("y: ",y)
            dwg.add(dwg.line((math.fabs(xorg), math.fabs(yorg)), (math.fabs(x), math.fabs(y)), stroke=svgwrite.rgb(10, 10, 16, '%')))

            xorg = x
            yorg = y

        else :
            print("Le fichier n'est pas correcte")
            exit()

dwg.save()
print("finished")
