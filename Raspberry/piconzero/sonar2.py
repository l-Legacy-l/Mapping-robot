
#DEVANT ; trig 27 echo 22 // gauche : echo 17 trigger 18


"""File: echo_multi_sensor.py"""
# Import necessary libraries.
from time import sleep

from Bluetin_Echo import Echo

# Define pin constants
TRIGGER_PIN_1 = 27
ECHO_PIN_1 = 22
TRIGGER_PIN_2 = 18
ECHO_PIN_2 = 17
speed_of_sound = 315

while True:

	capteurDevant = Echo(TRIGGER_PIN1, ECHO_PIN1, speed_of_sound)
	samples = 5
	result = capteurDevant.read('cm',samples)
	print(result,'cm')
	capteurDevant.stop()
	capteurGauche = Echo(TRIGGER_PIN2, ECHO_PIN2, speed_of_sound)
	samples = 5
	result = capteurGauche.read('cm',samples)
	print(result,'cm')
	capteurGauche.stop()
	time.sleep(1)