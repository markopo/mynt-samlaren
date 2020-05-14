import pgzrun
from random import randint

WIDTH = 400
HEIGHT = 400
summa = 0
spelet_slut = False

rav = Actor("fox")
rav.pos = 100, 100

mynt = Actor("coin")
mynt.pos = 200, 200

def draw():
    screen.clear()
    screen.fill("green")
    rav.draw()
    mynt.draw()
    screen.draw.text("Summa: " + str(summa), color="black", topleft=(10,10))


def placera_mynt():
    print("placera mynt")


def tiden_slut():
    print("tiden slut")


def update():
    placera_mynt()
    


pgzrun.go()    
