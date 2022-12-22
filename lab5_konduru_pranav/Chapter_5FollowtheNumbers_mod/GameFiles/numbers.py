# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 15:50:09 2022

@author: chris.pham
"""

import pgzrun
#import pygame
import pgzero
from pgzero.builtins import Actor
from random import randint

WIDTH = 400
HEIGHT = 400

#for debug
dot = Actor("dot")

#Set up the lists
dots = []
lines = []

next_dot = 0

number_of_dots = 15
for dot in range(0,number_of_dots):     #More dots feature added here
    actor = Actor("dot")
    actor.pos = randint(20, WIDTH-20), randint(20, HEIGHT-20)
    dots.append(actor)
    
def draw():
    screen.fill("black")
    number = 1
    for dot in dots:
        screen.draw.text(str(number), (dot.pos[0], dot.pos[1] + 12))  
        dot.draw()
        number = number + 1
    for line in lines:
        screen.draw.line(line[0], line[1], (200, 200, 100))

def on_mouse_down(pos):
    global next_dot
    global lines
    global number_of_dots
    #The next 2 lines are for debug, see the console printout
    """
    if dot.collidepoint(pos):
        print("Ouch!")
    """
    
    if dots[next_dot].collidepoint(pos):
        if next_dot:
            lines.append((dots[next_dot-1].pos, dots[next_dot].pos))
        next_dot = next_dot + 1
    elif next_dot == len(dots):
        print("The End")
        raise SystemExit()
    else:
        lines = []          #No more chance feature
        next_dot = 0
        print("Game Over")
        raise SystemExit()
        
pgzrun.go()