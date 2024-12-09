from os import system
from sys import platform


def clear():
    if platform.startswith("win"):
        system("cls")
    else:
        system("clear")


def affiche():  # Pour faire jolie
    length = int(longueur * 1.5)
    print()

    nombre = 0

    print("╭", end="")
    print("─" * ((longueur * 2) + 1), end="")
    print("╮", end="")
    print()
    for ligne in jeu:
        nombre += 1
        print("│ ", end="")
        for case in ligne:
            if case == 0:
                print(f"{GREY}·{RESET}", end=" ")
            elif case == 1:
                pass
        print("│", end="")
        print()

    print("╰", end="")
    print("─" * ((longueur * 2) + 1), end="")
    print("╯")

    print("\n")


def jeu_init(longueur, hauteur):
    jeu = []
    for i in range(longueur):
        jeu.append([])
        for j in range(hauteur):
            jeu[i].append(0)

    return jeu


clear()

ennemis = int(input("Nombres de fantômes (x) > 1:\n"))
clear()
longueur = int(input("Longueur du tableau > 2:\n"))
clear()
hauteur = int(input("Hauteur du tableau > 0:\n"))
jeu = jeu_init(longueur, hauteur)

YELLOW = "\033[33m"
RED = "\033[91m"
GREY = "\033[90m"
BLUE = "\033[34m"
RESET = "\033[0m"
