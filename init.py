from os import system
from sys import platform
from time import sleep
import random

windows = platform.startswith("win")

if windows:
    import msvcrt
else:
    import sys
    import termios
    import tty


# fonction
def affiche_refresh(fps):
    clear()
    affiche()
    sleep(1 / fps)


def clear():
    if windows:
        system("cls")
    else:
        system("clear")


YELLOW = "\033[33m"  # Les couleurs
PURPLE = "\033[35m"
RED = "\033[91m"
GREY = "\033[90m"
BLUE = "\033[34m"
RESET = "\033[0m"  # Annule la couleur


def locatePacman():
    for i in range(len(jeu)):
        for j in range(len(jeu[0])):
            if jeu[i][j] == 2:
                return j, i  # x, y
    return False

def locateFantomes(): # localiser un fantomes pour tuer pacman
    fantomes = []
    for i in range(len(jeu)):
        for j in range(len(jeu[0])):
            if jeu[i][j] == 3 or jeu[i][j] == 4 or jeu[i][j] == 3 :
                fantomes.append([i, j])  # y, x

    return fantomes

def locatefantomesMV(p): #localiser un fantomes particulier
    for i in range(len(jeu)):
        for j in range(len(jeu[0])):
            if jeu[i][j] == p:
                return j, i  # x, y
    return False

def pacmanMouvement(pacmanPosX, pacmanPosY, a, b):
    if jeu[pacmanPosY + b][pacmanPosX + a] == 0:
        jeu[pacmanPosY + b][pacmanPosX + a] = 2
        jeu[pacmanPosY][pacmanPosX] = 0
    elif (
        jeu[pacmanPosY + b][pacmanPosX + a] == 3
        or jeu[pacmanPosY + b][pacmanPosX + a] == 4
    ):
        jeu[pacmanPosY][pacmanPosX] = jeu[pacmanPosY + b][pacmanPosX + a]


def fantomeMouvement(fantomesPosX, fantomesPosY, a, b , fantome):
    if jeu[fantomesPosY + b][fantomesPosX + a] == 0:
        jeu[fantomesPosY + b][fantomesPosX + a] = fantome
        jeu[fantomesPosY][fantomesPosX] = 0

def fantomekill():  #le truc pour tuer le pacman 
    fantomes = locateFantomes()

    if len(fantomes) == 0:
        return True

    for fantome in fantomes:
        if jeu[fantome[0]][fantome[1]] == 2 and PacmanPowered:
            return False
        elif jeu[fantome[0]][fantome[1]] == 2 and not PacmanPowered:
            jeu[fantome[0]][fantome[1]] = 0
            return None

def affiche():  # Pour faire jolie
    nombre = 0
    longueur = int(len(jeu))
    print("╭", end="")
    print("─" * int(longueur * 2 + 5), end="")
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
                if PacmanPowered:
                    print("ᗤ", end=" ")
                else:
                    print(f"{YELLOW}ᗤ{RESET}", end=" ")

            elif case == 3:
                print(f"{RED}ᗣ{RESET}", end=" ")
            elif case == 4:
                print(f"{PURPLE}ᗣ{RESET}", end=" ")
            else:
                print("  ", end="")
        print("│", end="")
        print()

    print("╰", end="")
    print("─" * int(longueur * 2 + 5), end="")
    print("╯")

    print("\n")

def UserInputGame(code):
    if not locatePacman():
        return

    pacmanPosX, pacmanPosY = locatePacman()

    if code == 122:  # z
        pacmanMouvement(pacmanPosX, pacmanPosY, 0, -1)
    elif code == 113:  # q
        pacmanMouvement(pacmanPosX, pacmanPosY, -1, 0)
    elif code == 115:  # s
        pacmanMouvement(pacmanPosX, pacmanPosY, 0, 1)
    elif code == 100:  # d
        pacmanMouvement(pacmanPosX, pacmanPosY, 1, 0)
    elif code == 81:  # Q
        clear()
        print("Quit le jeu")
        exit()

def IAinput(mv,p):
    if not locatePacman():
        return
    
    fantomePosX, fantomePosY = locatefantomesMV(p)
    if mv == 1:  # haut
        fantomeMouvement(fantomePosX, fantomePosY, 0, -1,p)
    elif mv == 2:  # bas
        fantomeMouvement(fantomePosX, fantomePosY, -1, 0,p)
    elif mv == 3:  # gauche
        fantomeMouvement(fantomePosX, fantomePosY, 0, 1,p)
    elif mv == 4:  # droit
        fantomeMouvement(fantomePosX, fantomePosY,1, 0,p)

def IArandom(p):
    mv = random.randint(1,4)
    IAinput(mv,p)

def userInputUnix():
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

    if character:
        return UserInputGame(ord(character))
    else:
        return code


def UserInputWindows():
    if msvcrt.kbhit():
        character = msvcrt.getch()
        if character:
            return ord(character)
        else:
            return code




jeu = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

PacmanPowered = False

while True:
    affiche_refresh(fps=8)
    if windows:
        code = UserInputWindows()
    else:
        code = userInputUnix()

    UserInputGame(code)
    IArandom(4)
    win = fantomekill()
    if win:
        clear()
        print(f"""{YELLOW}
__   __           __        __
\ \ / /__  _   _  \ \      / / (_)____
 \ V / _ \| | | |  \ \ /\ / /  | |  _ \ 
  | | (_) | |_| |   \ V  V /   | | | | |
  |_|\___/ \____|    \_/\_/    |_|_| |_|
{RESET}""")
        exit()

    elif win == False or not locatePacman():
        clear()
        print(f"""{RED}
▄██   ▄    ▄██████▄  ███    █▄       ████████▄   ▄█     ▄████████ ████████▄
███   ██▄ ███    ███ ███    ███      ███   ▀███ ███    ███    ███ ███   ▀███
███▄▄▄███ ███    ███ ███    ███      ███    ███ ███▌   ███    █▀  ███    ███
▀▀▀▀▀▀███ ███    ███ ███    ███      ███    ███ ███▌  ▄███▄▄▄     ███    ███
▄██   ███ ███    ███ ███    ███      ███    ███ ███▌ ▀▀███▀▀▀     ███    ███
███   ███ ███    ███ ███    ███      ███    ███ ███    ███    █▄  ███    ███
███   ███ ███    ███ ███    ███      ███   ▄███ ███    ███    ███ ███    ███
 ▀█████▀   ▀██████▀  ████████▀       ████████▀  █▀     ██████████ ████████▀
{RESET}""")
        exit()
    elif win == None:
        pass
