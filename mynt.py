import pgzrun
from random import randint

WIDTH = 400
HEIGHT = 400
summa = 0
spelet_slut = False


max_x = WIDTH - 20
min_x = 20

min_y = 20
max_y = HEIGHT - 20

rav = Actor("fox")
rav.pos = 100, 100

mynt = Actor("coin")
mynt.pos = 20, 300



def tiden_slut():
    print("tiden slut")
    spelet_slut = True


def draw():
    screen.clear()
    screen.fill("green")
    rav.draw()
    mynt.draw()
    screen.draw.text("Summa: " + str(summa), color="black", topleft=(10,10))

def on_key_down(key):
    print(key)    



def update():

    if mynt.x < max_x:
            mynt.x = mynt.x + 1

    
    if keyboard.W:
        if rav.y > min_y:
            rav.y = rav.y - 2
    elif keyboard.S:
        if rav.y < max_y:
            rav.y = rav.y + 2 
    elif keyboard.A:
        if rav.x > min_x:
            rav.x = rav.x - 2
    elif keyboard.D:
        if rav.x < max_x:
            rav.x = rav.x + 2 

   
    


pgzrun.go()    
