#!/bin/python

import piconzero as pz
import time

# Espace entre le robot et le mur
gapmin = 5
gapmax = 10

onTrack = False

pz.init( )
while True:
    if front > gapmax && ! onTrack :
        pz.forward(50)
    elif ( gapmin < front < gapmax && side > gapmax ) || ( front > gapmax && side < gapmax ) :
        pz.spinRight(50)
        onTrack = True
