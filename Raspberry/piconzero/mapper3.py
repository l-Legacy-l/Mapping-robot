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
samples = 1

# Espace entre le robot et le mur
gapmin = 5
gapmax = 25

# Vitesse du robot
speed = 100

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
	print("devant = ",front," gauche = ",side)

	while front > 400 or side > 400:
		print("jai fait une boulette chef")
		pz.stop()
		samples = 2
		capteurDevant = Echo(TRIGGER_PIN1, ECHO_PIN1, speed_of_sound)
		front = capteurDevant.read('cm',samples)
		capteurDevant.stop()

		capteurGauche = Echo(TRIGGER_PIN2, ECHO_PIN2, speed_of_sound)
		side = capteurGauche.read('cm',samples)
		capteurGauche.stop()
		print("devant = ",front," gauche = ",side)
		samples = 1

	if onTrack :

		# Si rien devant et colle au mur
		if front > gapmax and gapmin < side < gapmax :
			print("devant ok mur colle")
			pz.forward(speed)

		# Si colle devant
		elif front < gapmax :
			print("colle devant")
			pz.forward(-50)
			time.sleep(0.5)
			pz.spinRight(90)
			time.sleep(1)
			pz.stop()

		# Si rien devant et rien sur le cote
		elif front > gapmax and side > gapmax :
			pz.stop()
			print("ok devant trop ecarte je me rapproche")
			if side < 2*gapmax: 
				pz.spinLeft(60)
				time.sleep(0.5)
				pz.forward(50)
				time.sleep(0.5)
				pz.spinLeft(60)
				time.sleep(0.5)
				pz.stop()
			else:
				pz.spinLeft(90)
				time.sleep(1)
				pz.stop()

		# Si trop proche du mur et rien en face
		if front > gapmax and side < gapmin :
			"print trop proche du mur je mecarte"
			pz.spinRight(50)
			time.sleep(0.5)
			pz.forward(50)
			time.sleep(0.5)
			pz.spinLeft(50)
			time.sleep(0.5)
			pz.stop()
	else :
		# Toujours tout droit tant qu'on approche pas d'un obstacle
		if front > gapmax and side > gapmax :
			if front < 80: 
				speed = 50
			print("tout droit debut")
			pz.forward(speed)
		# Quand on croise un obstacle on suit une piste
		else :
			pz.stop()
			"obstacle debut detecte"
			onTrack = True

	time.sleep(0.1)