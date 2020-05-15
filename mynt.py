import pgzrun
from random import randint

WIDTH = 600
HEIGHT = 600
summa = 0
spelet_slut = False
fox_speed = False

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

def place_coin():
    mynt.x = randint(20, (WIDTH - 20))
    mynt.y = randint(20, (HEIGHT - 20))    


def move_mynt():
    global current_direction, summa

    speed = 1

    if summa > 10:
        speed = summa / 10

    if current_direction == "right":
        if mynt.x < max_x:
            mynt.x = mynt.x + speed
        else:
            current_direction = get_new_direction()    
    elif current_direction == "left":
        if mynt.x > min_x:
            mynt.x = mynt.x - speed
        else:
            current_direction = get_new_direction()
        
    elif current_direction == "up":
        if mynt.y > min_y:
            mynt.y = mynt.y - speed 
        else:
            current_direction = get_new_direction()

    elif current_direction == "down":
        if mynt.y < max_y:
            mynt.y = mynt.y + speed
        else:
            current_direction = get_new_direction()         

def move_fox(): 
    global fox_speed

    speed = 2

    if fox_speed:
        speed = 4


    if keyboard.W:
        if rav.y > min_y:
            rav.y = rav.y - speed
    elif keyboard.S:
        if rav.y < max_y:
            rav.y = rav.y + speed 
    elif keyboard.A:
        if rav.x > min_x:
            rav.x = rav.x - speed
    elif keyboard.D:
        if rav.x < max_x:
            rav.x = rav.x + speed                

def space_pressed():
    global fox_speed

    sounds.nsmb_hurry_up.play()

    if fox_speed:
        fox_speed = False    
    else:
        fox_speed = True

def draw():
    screen.clear()
    screen.fill("green")
    rav.draw()
    mynt.draw()
    screen.draw.text("Summa: " + str(summa), color="black", topleft=(10,10))

def on_key_down(key):
    # print(key)
    pass    



def update():
    global summa, current_direction, spelet_slut

    if spelet_slut == False:
        move_mynt()
        move_fox()
 
        if rav.colliderect(mynt):
            sounds.nsmb_coin.play()
            summa = summa + 10
            place_coin()
            current_direction = get_new_direction()

        if keyboard.SPACE:
            space_pressed()

    if summa >= 100:
        spelet_slut = True
        sounds.smb_gameover.play()
  
   
    


pgzrun.go()    
