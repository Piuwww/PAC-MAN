#import
from os import system
from random import randint
from sys import platform
import time
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
                element ="C"
            print (element, end=" ")
        print()
    system("cls")
    time.sleep(0.001)
    return ""
    



#init
pac = 2
labi = [[1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,pac,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1]]   
#code
fin=False
while not (fin):
    affiche(labi)
