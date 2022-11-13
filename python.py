from array import *
import numpy 
import readchar
import os
import time
import pygame

playfield = numpy.chararray(shape=(15,40))
playfield = [
    ["****************************************"],
    ["* .....................................*"],
    ["*..*..*..*..*..*..*..*..*..*..*..*..*..*"],
    ["*..*..*..*..*..*..*..*..*..*..*..*..*..*"],
    ["*..*..*..*..*..*..*..*..*..*..*..*..*..*"],
    ["*..*..*..*..*..*..*..*..*..*..*..*..*..*"],
    ["*..*..*..*..*..*..*..*..*..*..*..*..*..*"],
    ["*......................................*"],
    ["*..*..*..*..*..*..*..*..*..*..*..*..*..*"],
    ["*..*..*..*..*..*..*..*..*..*..*..*..*..*"],
    ["*..*..*..*..*..*..*..*..*..*..*..*..*..*"],
    ["*..*..*..*..*..*..*..*..*..*..*..*..*..*"],
    ["*..*..*..*..*..*..*..*..*..*..*..*..*..*"],
    ["*......................................*"],
    ["****************************************"]
]

def draw_playfield():
    print("\033[0;31m")
    print("\n\n\n\n")
    for i in range(0, 15):
        print("\t\t")
        for j in range(0,40):
            print(playfield[i][j])
        print("\n")

food_collect=0
game_end=0
py=1   #these variables represent pacman coordinate
px=1   
gy1=1   #these variables represent ghosts coordinate
gx1=38
gy2=13
gx2=1   

def game_win():
    readchar
    os.system('clear')
    if(food_collect==500):
        print("\n\n\n\n\n\n\n\n\n")
        print("\t\t\t        Congratulation!\n")
        print("\t\t\t       You won the game!\n")
        print("\t\t\t     Your total score is"+food_collect)

def game_lose():
    if(food_collect<500):
        print("\n\n\n\n\n\n\n\n\n")
        print("\t\t\t          Better luck!\n")
        print("\t\t\t       You lose the game!\n")
        print("\t\t\t     Your total score is",+food_collect)

def move_ghost1():
    if(gy1==1 and gx1 > 1):
        gx1-=1 #this statement move 1st ghost coordinate to left side
    
    elif(gx1 == 1 and gy1 < 7):
        gy1+=1 #this statement move 1st ghost coordinate to down side
    
    elif(gy1 == 7 and gx1 < 38):
        gx1+=1 #this statement move 1st ghost coordinate to right side

    elif(gx1 == 38 and gy1 > 1):
        gy1-=1 #this statement move 1st ghost coordinate to up side

def move_ghost2():
    if(gy2 == 13 and gx2 < 38):
        gx2+=1 #this statement move 2nd ghost coordinate to right side

    elif(gx2 == 38 and gy2 > 7):
        gy2-=1 #this statement move 2nd ghost coordinate to up side

    elif(gy2 == 7 and gx2 > 1):
        gx2-=1 #this statement move 2nd ghost coordinate to left side
    
    elif(gx2 == 1 and gy2 < 13):
        gy2+=1 #this statement move 2nd ghost coordinate to down side

def user_inputs():
    for playfield in pygame.playfield.get():
        if(kbhit()):
            if(playfield.type == pygame.KEYDOWN):
                py+=1
            elif(playfield.type == pygame.K_RIGHT):
                px+=1
            elif(playfield.type == pygame.K_LEFT):
                px-=1
            elif(playfield.type == pygame.KEYUP):
                py-+1

def setup():
    for i in range(0, 15):
        for j in range(0,40):
            if(playfield[i][j]=='#'):
                playfield[i][j]=' '
            elif(playfield[i][j]=='@'):
                playfield[i][j]='.'
      
    if(playfield[py][px]=='.'):
        food_collect+=1
    if(playfield[py][px]=='*'):
        py=1
        px=1
    
    playfield[py][px]='#'
    playfield[gy1][gx1]='@'
    playfield[gy2][gx2]='@'

    if(playfield[py][px]=='@'):
        game_end=1

def delay():
    time.sleep(0.1)

def game_lost():
    if(playfield[py][px]=='@'):
        game_end=1

i=100
while(game_end!=1):
    readchar
    os.system(ls)
    setup()
    user_input()
    move_ghost1()
    move_ghost2()
    draw_playfield()
    game_lost()
    delay(0.1)
    if(i < 1000):
        i=i+100
    else:
        i=100

game_win()
game_lose()






