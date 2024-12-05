#import
from os import system
from random import randint
from sys import platform
import time
from msvcrt import getch,kbhit
#fonction
def clear():
    if platform.startswith("win"):
        system("cls")
    else:
        system("clear")

def affiche(liste):
    pac_l = 0
    pac_c = 0
    for i in range (len(liste)):
        for j in range (liste[i]) :
            if labi[i][j] == 0 :
                element =" "
            if labi[i][j] == 1:
                element ="□"
            if labi[i][j] == 2 :
                element ="ᗧ"
                pac_l = j
                pac_c = i
            print (element, end=" ")
        print()
    time.sleep(1/30)
    system("cls")
    return i , j

def aski():
    if kbhit():
        z = getch() #lecture touche
        code  = ord(z) # code ASCII
		
def mouvement(aski):
    i , j = affiche(labi)
    if aski == 122 :
        labi[i][j]
    if aski == 121 :
        labi[i][j]


    

#init
labi = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]   


#code
fin=False
while not (fin):
    affiche(labi)
