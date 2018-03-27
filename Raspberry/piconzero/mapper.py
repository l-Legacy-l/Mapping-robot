#!/bin/python

import piconzero as pz
import time

# Espace entre le robot et le mur
gapmin = 5
gapmax = 10

onTrack = False

pz.init( )
while True:
    if onTrack :

        # Si rien devant et collé au mur
        if front > gapmax && gapmin < side < gapmax :
            pz.forward(50)

        # Si collé au mur et collé devant
        elif front < gapmax && side < gapmax :
            pz.sideRight(50)

        # Si rien devant et rien sur le coté
        elif front > gapmax && side > gapmax :
            pz.sideLeft(50)

        # Si trop proche du mur et rien en face
        if front > gapmax && side < gapmin :
            pz.forward(50)




    else :
        if front > gapmax && side > gapmax :
            pz.forward(50)
        else
            onTrack = True
