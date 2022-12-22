# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 13:48:25 2022

@author: Pranav Konduru
"""

from random import randint
import pgzrun
#Allows game to run without crashing
from pgzero.builtins import Actor, clock, keys, music 

# Set the Stage

#Define size of the game window
WIDTH = 800
HEIGHT = 600
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2

#Contains list of dance movements
move_list = []
display_list = []

#Assigned integer values needed in the game
score_player1 = 0
score_player2 = 0   # Against friend
current_move = 0
count = 4
dance_length = 4
rounds = 0 # Added it for organization

#Flag varaiables that keep track of what's
#happening in game
say_dance = False
show_countdown = True
moves_complete = False
game_over = False

#Add the Actors

#Dancer appears when game starts
dancer = Actor("dancer-start")
dancer.pos = CENTER_X + 5, CENTER_Y - 40

#Arrange color coded sequence
up = Actor("up")
up.pos = CENTER_X, CENTER_Y + 110
right = Actor("right")
right.pos = CENTER_X + 60, CENTER_Y + 170
down = Actor("down")
down.pos = CENTER_X, CENTER_Y + 230
left = Actor("left")
left.pos = CENTER_X - 60, CENTER_Y + 170

# Draw the Actors

def draw():
    #Tells python which global variable to use
    global game_over, score_player1, score_player2, say_dance
    global count, show_countdown 
    #Only runs when game is not over
    if not game_over:
        screen.clear()
        screen.blit("stage", (0, 0)) # Add background
        #Draw all actors in current position
        dancer.draw()
        up.draw()
        down.draw()
        right.draw()
        left.draw()
        #Prints score on top left
        screen.draw.text("Score First Player: " + \
                         str(score_player1), color="black", \
                         topleft=(10, 10))
        screen.draw.text("Score Second Player: " + \
                         str(score_player2), color="black", \
                         topright=(790, 10))
        if say_dance:
            screen.draw.text("Dance", color="black", \
                             topleft=(CENTER_X - 65, 150), \
                                 fontsize=60)
        if show_countdown:
            screen.draw.text(str(count), color="black", \
                             topleft=(CENTER_X - 8, 150), \
                                 fontsize=60)
    #Game Over
    else:
        screen.clear()
        screen.blit("stage", (0, 0))
        screen.draw.text("Score First Player: " + str(score_player1), color="black", \
                         topleft=(10,10))
        screen.draw.text("Score Second Player: " + \
                         str(score_player2), color="black", \
                         topright=(790, 10))
        screen.draw.text("GAME OVER!", color="black", \
                         topleft=(CENTER_X - 130, 220), fontsize=60)
        screen.draw.text("Song: Upbeat Ambient by makesound", color="black", \
                         topleft=(CENTER_X - 160, 280), fontsize=30)
        
    return

# Musical Statues

#set the Actors back to their original position
def reset_dancer():
    global game_over
    if not game_over:
        dancer.image = "dancer-start"
        up.image = "up"
        right.image = "right"
        down.image = "down"
        left.image = "left"
    return
#updates Actor to show new dancec move
def update_dancer(move):
    #Tell dancer which move to perform
    global game_over
    if not game_over:
        if move == 0:
            #highlights color of square for Up
            up.image = "up-lit"
            #Changes image of the dancer
            dancer.image = "dancer-up"
            clock.schedule(reset_dancer, 0.5)
        elif move == 1:
            right.image = "right-lit"
            dancer.image = "dancer-right"
            #Hold move for half second
            clock.schedule(reset_dancer, 0.5)
        elif move == 2:
            down.image = "down-lit"
            dancer.image = "dancer-down"
            clock.schedule(reset_dancer, 0.5)
        else:
            left.image = "left-lit"
            dancer.image = "dancer-left"
            clock.schedule(reset_dancer, 0.5)
    return
#display latest sequence of moves 
def display_moves():
    global move_list, display_list, dance_length
    global say_dance, show_countdown, current_move
    #checks if the list od dance moves has something in it
    if display_list:
        #stores first move in display_list
        this_move = display_list[0]
        #removes first item from display_list 
        #so that seccond item will now be at position 0
        display_list = display_list[1:]
        if this_move == 0:
            update_dancer(0)
            clock.schedule(display_moves, 1)
        elif this_move == 1:
            update_dancer(1)
            clock.schedule(display_moves, 1)
        elif this_move == 2:
            update_dancer(2)
            #schedules a call to display_moves in one second
            clock.schedule(display_moves, 1)
        else:
            update_dancer(3)
            clock.schedule(display_moves, 1)
    else:
        say_dance = True # tells draw function to display
                            # dance
        show_countdown = False  #sets show_countdown to false
    return
#generate list of dance moves
def generate_moves():
    global move_list, dancne_length, count
    global show_countdown, say_dance
    count = 4
    move_list = []
    say_dance = False
    for move in range(0, dance_length):
        #assings numbers at random
        rand_move = randint(0, 3)
        move_list.append(rand_move)
        display_list.append(rand_move)
        
        #tells function draw() to diplay
        #value in count to creat countdown
        show_countdown = True
    countdown()
    return
#display countdown before sequence of moves
def countdown():
    global count, game_over, show_countdown
    if count > 1:
        count = count - 1
        #Schedules anoter call for countdown function
        #in 1 second
        clock.schedule(countdown, 1)
    else:
        #removes countdown from screen if count is less
        #than or equal to 1
        show_countdown = False
        display_moves()
    return
#Go to the next move
def next_move():
    #current_move identifies which move
    #you are dealing with
    global dance_length, current_move, moves_complete
    if current_move < dance_length - 1:
        current_move = current_move + 1
    else:
        moves_complete = True
    return
#Make program react when key is pressed for both players
def on_key_up(key):
    global score_player1, score_player2, game_over, move_list, current_move
    if key == keys.UP:
        update_dancer(0)
        #Score on each move
        if move_list[current_move] == 0:
            score_player1 = score_player1 + 1
            next_move()
        else:
            game_over = True
    #for W key
    elif key == keys.W:
        update_dancer(0)
        #Score on each move
        if move_list[current_move] == 0:
            score_player2 = score_player2 + 1
            next_move()
        else:
            game_over = True
    elif key == keys.RIGHT:
        update_dancer(1)
        if move_list[current_move] == 1:
            score_player1 = score_player1 + 1
            next_move()
        else:
            game_over = True
    #for D key
    elif key == keys.D:
        update_dancer(1)
        if move_list[current_move] == 1:
            score_player2 = score_player2 + 1
            next_move()
        else:
            game_over = True
    elif key == keys.DOWN:
        update_dancer(2)
        if move_list[current_move] == 2:
            score_player1 = score_player1 + 1
            next_move()
        else:
            game_over = True
    #for S key
    elif key == keys.S:
        update_dancer(2)
        if move_list[current_move] == 2:
            score_player2 = score_player2 + 1
            next_move()
        else:
            game_over = True
    elif key == keys.LEFT:
        #Each time arrow key is pressed, 
        #update_dancer function is called
        #to perform relevant moves
        update_dancer(3)
        if move_list[current_move] == 3:
            score_player1 = score_player1 + 1
            next_move()
        else:
            game_over = True
    #for A key
    elif key == keys.A:
        #Each time arrow key is pressed, 
        #update_dancer function is called
        #to perform relevant moves
        update_dancer(3)
        if move_list[current_move] == 3:
            score_player2 = score_player2 + 1
            next_move()
        else:
            game_over = True
    return
generate_moves()
#music.play("vanishing-horizon")
music.play("upbeat_ambient")
#Built in pygame zero function
#
def update():
    global game_over, current_move, moves_complete, rounds
    global dance_length
    if not game_over:
        if moves_complete:
            #Tweak to increase dance
            #Every three dance rounds
            #The length of the dance moves increase 
            #by 1
            if ((rounds) % 1 == 0):
                dance_length = dance_length + 1
            generate_moves()
            moves_complete = False
            current_move = 0
            #generate new rounds
            rounds = rounds + 1
    else:
        music.stop()
pgzrun.go()