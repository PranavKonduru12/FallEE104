#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 16:08:54 2022

@author: pranavkonduru
"""
import pgzrun
import pygame
import pgzero
from pgzero.builtins import Actor, keyboard
from random import randint

#Screen size
WIDTH = 800
HEIGHT = 600

#Setting up balloon
balloon = Actor("balloon")
balloon.pos = 400, 300

#Obstacles
bird = Actor("bird-up")
bird.pos = randint(800, 1600), randint(10, 200) #Birds appear at random positions of x

house = Actor("house")      #Creates new actor using image of house
house.pos = randint(800, 1600), 460

tree = Actor("tree")
tree.pos = randint(800, 1600), 450

#Create global variables
bird_up = True  #Keep track of images used for bird actor
up = False      
game_over = False   
score = 0   #Keeps track of the player's score
number_of_updates = 0   #Keeps track of how many times game has updated

new_high_score = False # File handling tweak 

#Manage High Scores
def update_high_scores():
    global score, scores
    filename = r"high-scores.txt"
    
    scores = []
    
    #Get current high scores
    with open(filename, "r") as file:
        line = file.readline()
        high_scores = line.split()
        
        #Find highest scores
        for high_score in high_scores:
            if(score > int(high_score)):
                scores.append(str(score) + " ")
                score = int(high_score)
            else:
                scores.append(str(high_score) + " ")
            
        # Write high scores in file
        with open(filename, "w") as file:
            for high_score in scores:
                file.write(high_score)

#Displaying high score
def display_high_scores():
    screen.draw.text("HIGH SCORES", (350, 150), color="black")
    y = 175 # sets fire score's position on y-axis
    position = 1
    for high_score in scores:
        screen.draw.text(str(position) + ". " + high_score, (350, y), color="black")
        y += 25
        position += 1

def draw():
    
    #Adds background image of sky, clouds, and grass
    screen.blit("background", (0, 0))

    #Draw Actors on screen if game is not over
    if not game_over:
        balloon.draw()
        bird.draw()
        house.draw()
        tree.draw()
        screen.draw.text("Score: "+ str(score), (700, 5), color="black")
    else:
        #Show high score
        display_high_scores()

#Reacting to mouse clicks
def on_mouse_down():
    global up
    up = True
    balloon.y -= 50
    
def on_mouse_up():
    global up
    up = False

#Bird Flap
def flap():
    global bird_up
    if bird_up:
        bird.image = "bird-down"
        bird_up = False
    else:
        bird.image = "bird-up"
        bird_up = True

#Update function
def update():
    global game_over, score, number_of_updates
    speed = 2
    if not game_over:
        if not up:
            balloon.y += 1
        
        #Move bird
        if bird.x > 0:
            bird.x -= 3 #speed it up feature
            if number_of_updates == 9:
                flap()
                number_of_updates = 0
            else:
                number_of_updates += 1
        
        #Handle bird flying off screen
        else:
            bird.x = randint(80, 1600)
            bird.y = randint(10, 200)
            score += 1
            number_of_updates = 0
    
        # Move the house
        if house.right > 0:
            house.x -= 2
        else:
            house.x = randint(800, 1600) # places house in random position
            score += 1
    
        #Move the trees
        if tree.right > 0:
            tree.x -= 2
        else:
            tree.x = randint(800, 1600)
            score += 1
    
        #Keep it steady
        #Checks if balloon has touched top of the screen 
        if balloon.top < 0 or balloon.bottom > 560: 
            game_over = True
            update_high_scores()
    
        # Handle coillisions with obsticles
        if balloon.collidepoint(bird.x, bird.y) or \
            balloon.collidepoint(house.x, house.y) or \
            balloon.collidepoint(tree.x, tree.y):
                game_over = True # tells the program that game is over
                update_high_scores()
        
        #Space out obstacles
        if tree.x == house.x:
            tree.x = randint(bird.x, house.x)
            house.x = randint(bird.x, house.x)
            
        #Leveling up
        if score%5 == 0:
            bird.x -= speed * 2
            
            
            
pgzrun.go()


