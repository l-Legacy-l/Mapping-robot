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
samples = 2

# Espace entre le robot et le mur
gapAvant = 30
gapGauche = 30

# Vitesse du robot
speed = 50

# Le robot ne suis pas encore un mur au depart
onTrack = False

pz.init( )
front = 50
while True: 
		capteurDevant = Echo(TRIGGER_PIN1, ECHO_PIN1, speed_of_sound)
		front = capteurDevant.read('cm',samples)
		capteurDevant.stop()
		if front > gapAvant:
			print("Rien devant")
			
			pz.forward(speed)
			capteurGauche = Echo(TRIGGER_PIN2, ECHO_PIN2, speed_of_sound)
			side = capteurGauche.read('cm',samples)
			capteurGauche.stop()
			print("distance gauche = ",side)
		elif side > gapGauche: 
			print("Tournant a gauche detecte")
			pz.forward(speed)
			time.sleep(0.3)
			pz.spinLeft(91)
			time.sleep(1)
			pz.stop()
		time.sleep(0.1)
		
	print("Objet detecte, rotation")	
	pz.spinRight(65)
	time.sleep(1.3)
	pz.stop()
	capteurDevant = Echo(TRIGGER_PIN1, ECHO_PIN1, speed_of_sound)
	front = capteurDevant.read('cm',samples)
	capteurDevant.stop()

