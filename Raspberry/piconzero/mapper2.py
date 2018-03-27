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
samples = 3

# Espace entre le robot et le mur
gapmin = 5
gapmax = 10

# Vitesse du robot
speed = 75

# Le robot ne suis pas encore un mur au départ
onTrack = False

pz.init( )

while True:
	while front > 5:
		print("Rien devant")
		capteurDevant = Echo(TRIGGER_PIN1, ECHO_PIN1, speed_of_sound)
		front = capteurDevant.read('cm',samples)
		capteurDevant.stop()
		pz.forward(speed)
		
	print("Objet détecté, rotation")	
	pz.spinLeft(75)
	time.sleep(0.5)
	pz.stop()
	capteurDevant = Echo(TRIGGER_PIN1, ECHO_PIN1, speed_of_sound)
	capteurDevant = capteurDevant.read('cm',samples)
	capteurDevant.stop()


''' while True:
    capteurDevant = Echo(TRIGGER_PIN1, ECHO_PIN1, speed_of_sound)
    front = capteurDevant.read('cm',samples)
    capteurDevant.stop()
	
	
	
	
	

 capteurGauche = Echo(TRIGGER_PIN2, ECHO_PIN2, speed_of_sound)
    side = capteurGauche.read('cm',samples)
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
        # Toujours tout droit tant qu'on approche pas d'un obstacle
        if front > gapmax and side > gapmax :
            pz.forward(speed)
        # Quand on croise un obstacle on suit une piste
        else :
            onTrack = True

    time.sleep(1)
    pz.stop() '''
