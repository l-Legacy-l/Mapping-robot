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
gapmax = 25

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
		print("Erreur du capteur, nouvelle prise de donnees")
		pz.stop()
		samples = 3
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

		#detection paroi en face 
		if front < gapmax and front != 0 :
			print("Je detecte une paroi en face, je tourne a droite")
			pz.forward(-50)
			time.sleep(0.5)
			pz.spinRight(90)
			time.sleep(1)
			pz.forward(speed)

		#detection coin tournant a auche
		elif front > gapmax and side > 50:
			print("je detecte un tournant a gauche, je tourne a gauche")
			pz.forward(-50)
			time.sleep(0.5)
			pz.spinLeft(90)
			time.sleep(1)
			pz.forward(speed)

		#ici a developper fonction pour mettre robot // au mur a distance 20cm
		elif front > 75 and side < gapmax:
			print("Je longe un mur")
			deport = [] #creation tableau et stock des donnes laterales
			while front > 75 and (side < gapmax+15 and side != 0):
				sample = 4
				capteurDevant = Echo(TRIGGER_PIN1, ECHO_PIN1, speed_of_sound) #get donnee
				front = capteurDevant.read('cm',samples)
				capteurDevant.stop()
				capteurGauche = Echo(TRIGGER_PIN2, ECHO_PIN2, speed_of_sound)
				side = capteurGauche.read('cm',samples)
				capteurGauche.stop()
				print("fction devant = ",front," gauche = ",side)
				if side != 0 : deport.append(side)
				compar = len(deport)
				print("longueur du tableau",compar)
				if compar >= 2: #si deux donnes, comparaison 
					print("deport-1 = ",deport[-1], "deport -2 =", deport[-2])
					if deport[-1] > deport[-2]: #ici on a deport vers l'exterieur
						print("deport exterieur")
						deportInterieur = False #on determine dans quelle direction le robot devie
					else : 
						deportInterieur = True
						print("deport interieur")
					if deportInterieur == True : #calcul coef et deplacement
						coef = (deport[-2]-deport[-1])/10
						print("coef = ",coef)
						pz.spinRight(50)
						time.sleep(coef)
						pz.forward(50)
					elif deportInterieur == False :
						coef = (deport[-1]-deport[-2])/10
						print("coef = ",coef)
						pz.spinLeft(50)
						time.sleep(coef)
						pz.forward(50)
		
		else :
			pz.forward(speed)

	else :
		print("Debut de la sequence")
		# Toujours tout droit tant qu'on approche pas d'un obstacle
		if front > gapmax and (side > gapmax or side == 0):
			if front < 50: 
				speed = 40
				print("Mur a proximite, reduction de la vitesse")
			pz.forward(speed)
		# Quand on croise un obstacle on suit une piste
		else :
			pz.stop()
			"Premier mur detecte, debut de la sequence detection"
			onTrack = True

	time.sleep(0.1)
