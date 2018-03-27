#!/bin/python

import piconzero as pz
import time

# Espace entre le robot et le mur
gap = 5

pz.init( )
while True:
    if front < gap && side < gap :
        pz.forward(50)
