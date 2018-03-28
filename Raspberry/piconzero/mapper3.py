#!/bin/python

# Import des librairies
import piconzero as pz
import time
from Bluetin_Echo import Echo
from threading import Thread

# Definition des pins
TRIGGER_PIN1 = 27
ECHO_PIN1 = 22
TRIGGER_PIN2 = 18
ECHO_PIN2 = 17

speed_of_sound = 315
samples = 1

# Espace entre le robot et le mur
gapmin = 20
gapmax = 30

# Vitesse du robot
speed = 100

# Le robot ne suis pas encore un mur au depart
onTrack = False

pz.init( )
while True:

	# recuperation ultrson
	capteurDevant = Echo(TRIGGER_PIN1, ECHO_PIN1, speed_of_sound)
	front = capteurDevant.read('cm',samples)
	capteurDevant.stop()

	capteurGauche = Echo(TRIGGER_PIN2, ECHO_PIN2, speed_of_sound)
	side = capteurGauche.read('cm',samples)
	capteurGauche.stop()
	print("devant = ",front," gauche = ",side)

	#correction erreur distance > a 4metres
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
		paroi = False
	#boucle une fois avoir rejoint une paroi
	if onTrack :

		# Si rien devant, et il est centre entre 20 et 30cm du mur
		if (front > gapmax and front != 0) and gapmin < side < gapmax :
			print("j'avance devant libre mur 20 30")
			print(compteur.value)
			pz.forward(speed)

		# Si contact mur avant
		elif front < gapmax/2 and front != 0 :


			print("Je suis face a une paroi")
			pz.forward(-50)
			time.sleep(0.5)
			pz.spinRight(90)
			time.sleep(0.9)
			pz.stop()

		# s'ecarte du mur, mais pas trop 
		elif front > gapmax and 50 > side > gapmax*0.8 :
			pz.stop()
			print("je peux avancer mais je mecarte du mur, donc je me rapproche")

			if side < 50:
				pz.spinLeft(50)
				time.sleep(0.2)
				pz.forward(75)
				time.sleep(0.8)
				pz.stop()

			elif 50 < side < 75:
				print("je suis fort loin d'un mur")
				pz.spinLeft(90)
				time.sleep(0.9)
				pz.forward(90)
				time.sleep(0.5)
				pz.spinRight(90)
				time.sleep(0.9)
				pz.stop()

		#dans un coin
		elif front < gapmax and side < gapmax :
			print("je suis dans un coin, je tourne a droite")
			pz.forward(-50)
			time.sleep(0.5)
			pz.spinRight(90)
			time.sleep(0.9)
			pz.stop()
		# trop proche du mur
		elif front > gapmax and side < gapmin :
			print("je peux avancer mais je suis trop pres du mur, je mecarte")
			pz.spinRight(50)
			time.sleep(0.2)
			pz.forward(75)
			time.sleep(0.8)
			pz.spinLeft(50)
			time.sleep(0.2)
			pz.stop()

		# face a une parois, peut etre oblique, donc on lui fait recuperer sa trajectoire
		elif front < gapmax and side > gapmax : 
			print("je suis bloque ")
			pz.spinRight(50)
			time.sleep(0.2)
			pz.forward(50)
			time.sleep(0.4)
			pz.spinLeft(50)
			time.sleep(0.2)
			pz.stop()

		# face a un mur, 0 a gauche, on tourne a droite
		elif front < gapmax and side == 0:
			print("je suis face a un mur, 0 gauche, je tourne a droite ")
			pz.spinRight(50)
			time.sleep(0.2)
			pz.forward(50)
			time.sleep(0.4)
			pz.spinLeft(50)
			time.sleep(0.2)
			pz.stop()

		# grande distance devant, en cas de contour d'objet

		elif front == 0:
			pz.forward(speed)

		# objet contourne, tourner a gauche 
		elif front > gapmax and side > 50:
			print("je viens de contourner un obstacle, je tourne a gauche")
			pz.forward(50)
			time.sleep(0.2)
			pz.spinLeft(90)
			time.sleep(0.9)
			pz.forward(100)
			time.sleep(0.7)
			pz.stop()



	else :
		# Toujours tout droit tant qu'on approche pas d'un obstacle
		if front > gapmax and (side > gapmax or side == 0):
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