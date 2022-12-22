import pgzrun 
import pygame 
import pgzero #Reminder: pip install pgzero
from pgzero.builtins import Actor
from random import randint

apple = Actor("apple")  #initialize apple
orange = Actor("orange")  #initialize orange
#pineapple = Actor("pineapple") #initialize pineapple
pineapple = Actor("pineapple100x100") #using new pineapple picture

Hit=0   #initialize counter for hit
Miss=0  #initialize counter for miss

def draw(): # sets up the interface (first screen) when game starts
    screen.clear()  #clears screen
    apple.draw()    #place fruits in top-left corner
    orange.draw()
    pineapple.draw()
    #moved scoreboard to top right
    screen.draw.text("Hit: " +str(Hit) + " " +"Miss: " +str(Miss), color="white", topleft=(680,10)) #displays scoreboard



def place_apple(): #position/coordinates for placing apple on screen/interface
    apple.x = randint(10,800)   #picks random x coordinate from 10 to 800
    apple.y = randint(10,600)   #picks random y coordinate from 10 to 600


def place_orange(): #position/coordinates for placing orange on screen/interface
    orange.x = randint(40,800)  #picks random x coordinate from 40 to 800
    orange.y = randint(50,600)  #picks random y coordinate from 50 to 600


def place_pineapple():  #position/coordinates for placing pineapple on screen/interface
    pineapple.x = randint(80,800)   #picks random x coordinate from 80 to 800
    pineapple.y = randint(100,600)  #picks random y coordinate from 100 to 600    
    


def on_mouse_down(pos): #logic for mouse clicking
    global Hit #initialized global variables
    global Miss
    if apple.collidepoint(pos): #user clicks on apple actor
        #print("Good shot!")
        place_apple()           #call place_apple() function
        Hit=Hit+1               #update hit counter by increment of 1
        

    else:                       #does not click on apple actor
        #print("Missed!")
        Miss=Miss+1             #update miss counter by incremebnt of 1
        if randint(1,10)%2 :    #picks random integer from 1 to 10 for divident
            place_orange()      #if remainder is 0, then call place_orange()
        else:
            place_pineapple()   #if remainder is 0, then call place_orange()


pgzrun.go() # Program execution