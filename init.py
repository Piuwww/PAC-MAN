from os import system
from sys import platform
from time import sleep

windows = platform.startswith("win")

if windows:
    import msvcrt
else:
    import sys
    import termios
    import tty


# fonction
def affiche_refresh(a): #a c'est le refresh rate fréquence de màj
    for i in range (2):
        clear() 
        affiche()
        sleep(1/a)

def clear():
    if windows:
        system("cls")
    else:
        system("clear")


YELLOW = "\033[33m"  # Les couleurs
RED = "\033[91m"
GREY = "\033[90m"
BLUE = "\033[34m"

RESET = "\033[0m"  # Annule la couleur


def affiche():  # Pour faire jolie
    nombre = 0
    longueur = int(len(jeu))
    print("╭", end="")
    print("─" * int(longueur * 2.8), end="")
    print("╮", end="")
    print()
    for ligne in jeu:
        nombre += 1
        print("│ ", end="")
        for case in ligne:
            if case == 0:
                print(f"{GREY}·{RESET}", end=" ")
            elif case == 1:
                print(f"{BLUE}8{RESET}", end=" ")
            elif case == 2:
                print(f"{YELLOW}ᗤ{RESET}", end=" ")
            elif case == 3:
                print(f"{RED}ᗣ{RESET}", end=" ")
            elif case == 4:
                print("🍓", end=" ")
            else:
                print("  ", end="")
        print("│", end="")
        print()

    print("╰", end="")
    print("─" * int(longueur * 2.8), end="")
    print("╯")

    print("\n")


def UserInputGame(code):
    if code == 122:  # z
        return "z"
    elif code == 113:  # q
        return "q"
    elif code == 115:  # s
        return "s"
    elif code == 100:  # d
        return "d"
    elif code == 81:  # Q
        print("Quit le jeu")
        exit()


def userInputLinux():
    fd = sys.stdin.fileno()  # Ouvre un buffer/tty/terminal
    old_settings = termios.tcgetattr(fd)  # Prend les paramètres du buffer/tty
    try:
        tty.setraw(  # Ne print pas les charactères écrits, pas besoin de <enter>
            sys.stdin.fileno()
        )
        character = sys.stdin.read(1)  # Lis 1 seule charactère
    finally:
        termios.tcsetattr(  # Définis les paramètres du tty/buffer
            fd, termios.TCSADRAIN, old_settings
        )

    UserInputGame(ord(character))


def UserInputWindows():
    if msvcrt.kbhit():
        character = msvcrt.getch()
        UserInputGame(ord(character))


def check_mouvement(x,y):
    UserInputWindows()
    if "z" and jeu[x+1][y]==0:
        return True
    if "q" and 2[x][y-1]==0:
        return True
    if "s" and 2[x-1][y]==0:
        return True
    if "d" and 2[x][y+1]==0:
        return True
    else:
        return False

#def mouvement():


def jouer():
    affiche_refresh(60)
    UserInputWindows()



# init
jeu = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

while True:
    jouer()