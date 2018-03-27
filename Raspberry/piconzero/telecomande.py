#!/bin/python

import piconzero as pz
import sys
import readchar
import time

pz.init( )
while True:
    #touche = sys.stdin.read(1)
    touche = readchar.readchar()
    if touche == "w":
        pz.forward(50)
    elif touche == "s":
        pz.reverse(50)
    elif touche == "d":
        pz.spinRight(75)
    elif touche == "a":
        pz.spinLeft(75)
    elif touche == "q":
	exit()
    else:
        pz.stop()




