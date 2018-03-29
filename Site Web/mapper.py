#!/usr/bin/python

import sys
import svgwrite
import os
import time

path = sys.argv[1] + "/" + sys.argv[2]

if not os.path.exists(sys.argv[1]):
    os.makedirs(sys.argv[1])

dwg = svgwrite.Drawing(path + '.svg', profile='tiny')
dwg.add(dwg.line((0, 0), (10, 0), stroke=svgwrite.rgb(10, 10, 16, '%')))
dwg.add(dwg.line((49, 10), (11, 103), stroke=svgwrite.rgb(10, 10, 16, '%')))
dwg.add(dwg.line((0, 32), (42, 29), stroke=svgwrite.rgb(10, 10, 16, '%')))
dwg.add(dwg.line((39, 49), (17, 4), stroke=svgwrite.rgb(10, 10, 16, '%')))
dwg.add(dwg.text('Test', insert=(0, 10), fill='red'))
time.sleep(10)
dwg.save()
print("fini")
