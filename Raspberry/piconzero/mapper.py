#!/bin/python

import piconzero as pz
import time

# Espace entre le robot et le mur
gapmin = 5
gapmax = 10

onTrack = False

pz.init( )
while True:
    # Si rien devant et collé au mur
    if front > gapmax && gapmin < side < gapmax :
        pz.spinRight(50)
    # Si collé au mur et collé devant
    elif front < gapmax && side < gapmax :
        pz


    else :
        if front > gapmax && side > gapmax :
            pz.forward(50)
        else
            onTrack = True