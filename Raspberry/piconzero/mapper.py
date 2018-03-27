#!/bin/python

# Import des librairies
import piconzero as pz
import time
from Bluetin_Echo import Echo

# Définition des pins
TRIGGER_PIN1 = 27
ECHO_PIN1 = 22
TRIGGER_PIN2 = 18
ECHO_PIN2 = 17
speed_of_sound = 315
samples = 25

# Espace entre le robot et le mur
gapmin = 5
gapmax = 10

# Vitesse du robot
speed = 100

# Le robot ne suis pas encore un mur au départ
onTrack = False

pz.init( )
while True:
    capteurDevant = Echo(TRIGGER_PIN1, ECHO_PIN1, speed_of_sound)
    result = capteurDevant.read('cm',samples)
    print("capteur devant : ",result)
    front = result
    capteurDevant.stop()

    capteurGauche = Echo(TRIGGER_PIN2, ECHO_PIN2, speed_of_sound)
    result = capteurGauche.read('cm',samples)
    print("capteur gauche : ",result)
    side = result
    capteurGauche.stop()

    time.sleep(1)

    if onTrack :

        # Si rien devant et colle au mur
        if front > gapmax and gapmin < side < gapmax :
            pz.forward(speed)

        # Si colle devant
        elif front < gapmax :
            pz.spinRight(speed)

        # Si rien devant et rien sur le cote
        elif front > gapmax and side > gapmax :
            pz.spinLeft(speed)

        # Si trop proche du mur et rien en face
        if front > gapmax and side < gapmin :
            pz.spinRight(speed)

    else :
        if front > gapmax and side > gapmax :
            pz.forward(speed)
        else :
            onTrack = True

    time.sleep(1)
    pz.stop()
