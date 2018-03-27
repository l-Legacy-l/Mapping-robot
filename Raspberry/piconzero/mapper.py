#!/bin/python

import piconzero as pz
import time

# Espace entre le robot et le mur
gapmin = 5
gapmax = 10

pz.init( )
while True:
    if front > gapmax :
        pz.forward(50)
    elif gapmin < front < gapmax && side > gapmax :
        pz.spinRight(50)
