from array import *
import numpy 
import readchar
import os
import keyboard
import time

global playfield, food_collect, game_end, py, px, gy1, gx1, gy2, gx2

playfield = [
    "****************************************",
    "* .....................................*",
    "*..*..*..*..*..*..*..*..*..*..*..*..*..*",
    "*..*..*..*..*..*..*..*..*..*..*..*..*..*",
    "*..*..*..*..*..*..*..*..*..*..*..*..*..*",
    "*..*..*..*..*..*..*..*..*..*..*..*..*..*",
    "*..*..*..*..*..*..*..*..*..*..*..*..*..*",
    "*......................................*",
    "*..*..*..*..*..*..*..*..*..*..*..*..*..*",
    "*..*..*..*..*..*..*..*..*..*..*..*..*..*",
    "*..*..*..*..*..*..*..*..*..*..*..*..*..*",
    "*..*..*..*..*..*..*..*..*..*..*..*..*..*",
    "*..*..*..*..*..*..*..*..*..*..*..*..*..*",
    "*......................................*",
    "****************************************"
]
food_collect = 0
game_end = 0
py = 1   #these variables represent pacman coordinate
px = 1   
gy1 = 1   #these variables represent ghosts coordinate
gx1 = 38
gy2 = 13
gx2 = 1  


def draw_playfield():
    os.system("cls")
    for i in range(0, 14):
        print("\t\t")
        for j in range(0,39):
            print(playfield[i][j],end="")

def replace_char(str,index,new):
    return str[:index] + new + str[index+1:]

def game_win():
    os.system('cls')
    if(food_collect==500):
        print("\n\n\n\n\n\n\n\n\n")
        print("\t\t\t        Congratulation!\n")
        print("\t\t\t       You won the game!\n")
        print("\t\t\t     Your total score is"+food_collect)

def game_lose():
    os.system('cls')
    if(food_collect<500):
        print("\n\n\n\n\n\n\n\n\n")
        print("\t\t\t          Better luck!\n")
        print("\t\t\t       You lose the game!\n")
        print("\t\t\t     Your total score is",+food_collect)

def move_ghost1():
    global gx1,gy1
    if(gy1==1 and gx1 > 1):
        gx1-=1 #this statement move 1st ghost coordinate to left side
    
    elif(gx1 == 1 and gy1 < 7):
        gy1+=1 #this statement move 1st ghost coordinate to down side
    
    elif(gy1 == 7 and gx1 < 38):
        gx1+=1 #this statement move 1st ghost coordinate to right side

    elif(gx1 == 38 and gy1 > 1):
        gy1-=1 #this statement move 1st ghost coordinate to up side

def move_ghost2():
    global gx2,gy2
    if(gy2 == 13 and gx2 < 38):
        gx2+=1 #this statement move 2nd ghost coordinate to right side

    elif(gx2 == 38 and gy2 > 7):
        gy2-=1 #this statement move 2nd ghost coordinate to up side

    elif(gy2 == 7 and gx2 > 1):
        gx2-=1 #this statement move 2nd ghost coordinate to left side
    
    elif(gx2 == 1 and gy2 < 13):
        gy2+=1 #this statement move 2nd ghost coordinate to down side

def user_inputs():
    global px,py
    if(keyboard.is_pressed('w')):
        py-=1
    elif(keyboard.is_pressed('d')):
        px+=1

    elif(keyboard.is_pressed('a')):
        px-=1
    if(keyboard.is_pressed('s')):
        py+=1


def setup():
    global px,py,food_collect,game_end
    for i in range(0, 14):
        for j in range(0,39):
            if(playfield[i][j]=='#'):
                playfield[i]=replace_char(playfield[i], j, '')
            elif(playfield[i][j]=='@'):
                playfield[i]=replace_char(playfield[i], j, '.')
      
    if(playfield[py][px]=='.'):
        food_collect+=1
    if(playfield[py][px]=='*'):
        py=1
        px=1
    
    playfield[py]=replace_char(playfield[py],px,'#')
    playfield[gy1]=replace_char(playfield[gy1],gx1,'@')
    playfield[gy2]=replace_char(playfield[gy2],gx2,'@')

def delay():
    time.sleep(0.1)

def game_lost():
    global game_end
    if(playfield[py][px]=='@'):
        game_end=1

i=100
temp=True
while(game_end!=1):
    if(temp==True):
        char=readchar.readchar()
    user_inputs()
    setup()
    move_ghost1()
    move_ghost2()
    draw_playfield()
    game_lost()
    delay()
    if(i < 1000):
        i=i+100
    else:
        i=100
    temp = False

game_win()
game_lose()

