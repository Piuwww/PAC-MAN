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
    for i in range (len(liste)):
        for element in liste[i]:
            if element == 0 :
                element =" "
            if element == 1:
                element ="□"
            if element == 2 :
                element ="ᗧ"
            print (element, end=" ")
        print()
    time.sleep(1/30)
    system("cls")
    return ""


#init
labi = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]   
#code
fin=False
j = len(labi) /2
i = len(labi)
while not (fin):
    affiche(labi)
    if kbhit():
        z = getch() #lecture touche
        code  = ord(z) # code ASCII
        print (code)

        if code == 122:    #bon code 122 = z mais crash
            labi[j][i]=0
            j = j+1
            labi[j][i]=2
            clear
            affiche(labi)

while not (fin):
    affiche(labi)
