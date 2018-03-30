# Picon Zero Motor Test
# Moves: Forward, Reverse, turn Right, turn Left, Stop - then repeat
# Press Ctrl-C to stop
#
# To check wiring is correct ensure the order of movement as above is correct

import piconzero as pz, time

#======================================================================
# Reading single character by forcing stdin to raw mode
import sys
import tty
import termios
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
            i = pz.readInput(2)  
            if i != j :  
                self.value = self.value + 1  
                print(self.value)  
            time.sleep(0.01)  
    def stop(self):  
        self.on = False  
    def zero(self): 
        self.value = 0 
    def get(self): 
        return self.value 
  
c = compteur()  
f = open("output", "w")

def readchar():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    if ch == '0x03':
        raise KeyboardInterrupt
    return ch

def readkey(getchar_fn=None):
    getchar = getchar_fn or readchar
    c1 = getchar()
    if ord(c1) != 0x1b:
        return c1
    c2 = getchar()
    if ord(c2) != 0x5b:
        return c1
    c3 = getchar()
    return chr(0x10 + ord(c3) - 65)  # 16=Up, 17=Down, 18=Right, 19=Left arrows

# End of single character reading
#======================================================================

speed = 60

print "Tests the motors by using the arrow keys to control"
print "Use , or < to slow down"
print "Use . or > to speed up"
print "Speed changes take effect when the next arrow key is pressed"
print "Press Ctrl-C to end"
print

pz.init()

prev = 0 # 0 pour tout droit, 1 pour rotation a droite et 2 pour rotation a gauche
# code a ajouter avant chaque rotation a gauche
def gauche():
    if(prev == 0):
        f.write("L " + c.get() + "\n")
    elif(prev == 1):
        f.write("D " + c.get() + "\n")
    prev = 2
# code a ajouter avant chaque rotation a droite
def droite():
    if(prev == 0):
        f.write("L " + c.get() + "\n")
    elif(prev == 2):
        f.write("G " + c.get() + "\n")
    prev = 1
# code a ajouter avant chaque mise en route (sans compter les ajustement)
def toutDroit():
    if(prev == 1):
        f.write("D " + c.get() + "\n")
    elif(prev == 2):
        f.write("G " + c.get() + "\n")
    prev = 1
# main loop
try:
    while True:
        keyp = readkey()
        if keyp == 'w' or ord(keyp) == 16:
            toutDroit()
            pz.forward(speed)
            print 'Forward', speed
        elif keyp == 'z' or ord(keyp) == 17:
            c.zero()
            pz.reverse(speed)
            prev = 1
            print 'Reverse', speed
        elif keyp == 's' or ord(keyp) == 18:
            droite()
            c.zero()
            pz.spinRight(speed)
            prev = 1
            print 'Spin Right', speed
        elif keyp == 'a' or ord(keyp) == 19:
            gauche()
            c.zero()
            pz.spinLeft(speed)
            prev = 1
            print 'Spin Left', speed
        elif keyp == '.' or keyp == '>':
            speed = min(100, speed+10)
            print 'Speed+', speed
        elif keyp == ',' or keyp == '<':
            speed = max (0, speed-10)
            print 'Speed-', speed
        elif keyp == ' ':
            c.zero()
            pz.stop()
            print 'Stop'
        elif ord(keyp) == 3:
            break

except KeyboardInterrupt:
    print

finally:
    pz.cleanup()
    
