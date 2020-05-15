import pgzrun
from random import randint

WIDTH = 600
HEIGHT = 600
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

directions = [ "up", "down", "left", "right" ]
current_direction = "right"



def tiden_slut():
    print("tiden slut")
    spelet_slut = True


def get_new_direction():
    index = randint(0, len(directions)-1)
    return directions[index]


def move_mynt():
    global current_direction

    if current_direction == "right":
        if mynt.x < max_x:
            mynt.x = mynt.x + 1
        else:
            current_direction = get_new_direction()    
    elif current_direction == "left":
        if mynt.x > min_x:
            mynt.x = mynt.x - 1
        else:
            current_direction = get_new_direction()
        
    elif current_direction == "up":
        if mynt.y > min_y:
            mynt.y = mynt.y -1 
        else:
            current_direction = get_new_direction()

    elif current_direction == "down":
        if mynt.y < max_y:
            mynt.y = mynt.y + 1
        else:
            current_direction = get_new_direction()         

def move_fox(): 
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


def draw():
    screen.clear()
    screen.fill("green")
    rav.draw()
    mynt.draw()
    screen.draw.text("Summa: " + str(summa), color="black", topleft=(10,10))

def on_key_down(key):
    print(key)    



def update():
    move_mynt()
    move_fox()
 

   
    


pgzrun.go()    
