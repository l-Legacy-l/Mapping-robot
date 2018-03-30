#!/bin/python
#gerer le post tournant a gauche pour quil sarrete quand il nest plus proche de l'objet
# Import des librairies
import piconzero as pz
import time
from Bluetin_Echo import Echo
from threading import Thread

class compteur(Thread):  
    def __init__(self):  
        Thread.__init__(self)  
        self.daemon = True  
        self.value = 0  
        self.on = False  
        self.start()  
    def run(self):  
        self.on = True  
        i = 0  
        j = 0  
        while(self.on):  
            j = i  
            i = (pz.readInput(2) + pz.readInput(3))/2
            if i != j :  
                self.value = self.value + 1  
            time.sleep(0.01)  
    def stop(self):  
        self.on = False  
    def zero(self): 
        self.value = 0 
    def get(self): 
        return str(self.value)
  
c = compteur()  

f = open("output", "w")

prev = 0 # 0 pour tout droit, 1 pour rotation a droite et 2 pour rotation a gauche
# code a ajouter avant chaque rotation a gauche
def gauche():
    global prev
    if(prev == 0):
        f.write("L " + c.get() + "\n")
    elif(prev == 1):
        f.write("D " + c.get() + "\n")
    prev = 2
    c.zero()
# code a ajouter avant chaque rotation a droite
def droite():
    global prev
    if(prev == 0):
        f.write("L " + c.get() + "\n")
    elif(prev == 2):
        f.write("G " + c.get() + "\n")
    prev = 1
    c.zero()
# code a ajouter avant chaque mise en route (sans compter les ajustement)
def toutDroit():
    global prev
    if(prev == 1):
        f.write("D " + c.get() + "\n")
    elif(prev == 2):
        f.write("G " + c.get() + "\n")
    prev = 0
    c.zero()
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
#time.sleep(30)
pz.init( )
try:

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
		while front > 1000 or side > 1000:
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
			if front < 50 and front != 0 :
				toutDroit()
				pz.forward(40)
				while front < gapmax and front != 0:
					print(front,"Je detecte une paroi en face")
					while gapmax > front > 10 : 
						print("je peux me rapprocher distance = ",front)
						toutDroit()
						pz.forward(60)
						time.sleep(0.2)
						pz.stop()
						capteurDevant = Echo(TRIGGER_PIN1, ECHO_PIN1, speed_of_sound)
						front = capteurDevant.read('cm',samples)
						capteurDevant.stop()
					if front < 10 : 
						pz.stop()
						pz.forward(-50)
						time.sleep(0.5)
						droite()
						pz.spinRight(95)
						time.sleep(1)
						toutDroit()
						pz.forward(50)
					capteurDevant = Echo(TRIGGER_PIN1, ECHO_PIN1, speed_of_sound)
					front = capteurDevant.read('cm',samples)
					capteurDevant.stop()	


			elif front == 0 and side == 0 :
				gauche()
				pz.spinLeft(90)
				time.sleep(1)
				toutDroit()
				pz.forward(60)
			#detection coin tournant a auche
			elif front > gapmax and ( side > 50 or side == 0 and side <401):
				print("je detecte un tournant a gauche, je tourne a gauche")
				pz.forward(-65)
				time.sleep(0.2)
				gauche()
				pz.spinLeft(90)
				time.sleep(1.1)
				toutDroit()
				pz.forward(75)
				time.sleep(1)

			#ici a developper fonction pour mettre robot // au mur a distance 20cm
			elif front > 75 and (side < gapmax and side != 0):
				print("Je longe un mur")
				deport = [] #creation tableau et stock des donnes laterales
				while front > 75 and (side < gapmax+25 and side != 0):
					sample = 4
					capteurDevant = Echo(TRIGGER_PIN1, ECHO_PIN1, speed_of_sound) #get donnee
					front = capteurDevant.read('cm',samples)
					capteurDevant.stop()
					capteurGauche = Echo(TRIGGER_PIN2, ECHO_PIN2, speed_of_sound)
					side = capteurGauche.read('cm',samples)
					capteurGauche.stop()
					print("fction devant = ",front," gauche = ",side)


					if len(deport) < 2 and side > 35:

						pz.spinLeft(90)
						time.sleep(1)
						pz.forward(80)
						time.sleep(0.4)
						pz.spinRight(90)
						time.sleep(1)
						pz.forward(40)

					if side != 0: deport.append(side)
					compar = len(deport)
					print("longueur du tableau",compar)
					if side < 10 and side != 0 :
						print("Je suis trop proche",side)
						#justOblique = False
						if (20-side)/10 > 0.1 : 
							pz.spinRight(65)
							time.sleep(((20-side)/10)*0.6)
							pz.forward(60)
							time.sleep(0.2)
							pz.spinLeft(65)
							time.sleep(((20-side)/10)*0.6)
							pz.forward(50)
							time.sleep(0.8)
					elif 40> side > 20 and side != 0 :
						print("je suis trop loin",side)
						if (side-20)/10 > 0.1 : 
							pz.spinLeft(65)
							time.sleep(((side-20)/10)*0.6)
							pz.forward(60)
							time.sleep(0.4)
							pz.spinRight(50)
							time.sleep(((side-20)/10)*0.6)
							pz.forward(50)
							time.sleep(0.8)
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

finally :
	pz.stop()
