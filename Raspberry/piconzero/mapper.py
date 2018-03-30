#!/bin/python

# Import des librairies
import piconzero as pz
import time
from Bluetin_Echo import Echo

# Definition des pins
TRIGGER_PIN1 = 27
ECHO_PIN1 = 22
TRIGGER_PIN2 = 18
ECHO_PIN2 = 17

speed_of_sound = 315
samples = 3

# Espace entre le robot et le mur
gapmin = 30
gapmax = 50

# Vitesse du robot
speed = 60

# Le robot ne suis pas encore un mur au depart
onTrack = False

pz.init( )
while True:
	capteurDevant = Echo(TRIGGER_PIN1, ECHO_PIN1, speed_of_sound)
	front = capteurDevant.read('cm',samples)
	capteurDevant.stop()

	capteurGauche = Echo(TRIGGER_PIN2, ECHO_PIN2, speed_of_sound)
	side = capteurGauche.read('cm',samples)
	capteurGauche.stop()
	print("Capteur devant = ",front," capteur gauche = ",side)
	time.sleep(0.1)

    if onTrack :

        # Si rien devant et colle au mur
        if front > gapmin and gapmin < side < gapmax :
			print("rien devant j'avance")
            pz.forward(speed)

        # Si colle devant
        elif front < gapmin :
			print("objet détecté, je tourne à droite 90°")
			pz.spinRight(91)
			time.sleep(1)
			pz.stop()

        # Si rien devant et rien sur le cote
        elif front > gapmax and side > gapmax :
			print("plus de mur à ma gauche, je tourne à gauche 90°")
			pz.spinLeft(91)
			time.sleep(1)
			pz.stop()

        # Si trop proche du mur et rien en face
        if front > gapmax and side < gapmin :
			print("Je suis trop proche du mur, je m'écarte")
			pz.spinRight(60)
			time.sleep(0.5)
			pz.stop()

    else :
        # Toujours tout droit tant qu'on approche pas d'un obstacle
        if front > gapmax and side > gapmax :
			print("Rien devance, j'avance boucle2")
            pz.forward(speed)
        # Quand on croise un obstacle on suit une piste
        else :
			print("Obstacle détecté boucle2")
            onTrack = True

    time.sleep(0.1)
