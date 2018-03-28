#!/bin/python

import re
import svgwrite
import math

ratio = 90/40

dwg = svgwrite.Drawing('test.svg', profile='tiny')
angle = 0
line = 0
xorg = 0
yorg = 0

with open("exemple", "r") as f :
    for line in f :
        if re.match("^A", line) is not None :
            angle = re.findall("([0-9]+)", line)
            angle = angle * ratio
            print("Angle : ", angle)
        elif re.match("^L", line) is not None :
            line = re.findall("([0-9]+)", line)
            line = line * ratio
            print("Line : ", line)
        else :
            print("Le fichier n'est pas correcte")
            exit()

        if(angle != 0 and line != 0) :
            x = sin(angle) * line #socathoa
            y = cos(angle) * line #socathoa
            dwg.add(dwg.line((0, 0), (10, 0), stroke=svgwrite.rgb(10, 10, 16, '%')))

            xorg = x
            yorg = y

dwg.save()

