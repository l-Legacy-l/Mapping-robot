#! /usr/bin/env python

import piconzero as pz, time

pz.init()

i = 0
j = 0
turns = 0

while True:
    j = i
    i = pz.readInput(2)
    if i != j :
        turns = turns + 1
        print(turns)
    time.sleep(0.01)
