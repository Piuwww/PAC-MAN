#import
from os import system
from random import randint
from sys import platform
from time import sleep, time
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

affiche(labi)
input()
