from os import system
from sys import platform
from time import sleep

windows = platform.startswith("win")

if windows:
    import msvcrt
    import random
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
RED = "\033[91m"
GREY = "\033[90m"
BLUE = "\033[34m"
RESET = "\033[0m"  # Annule la couleur


def locatePacman():
    for i in range(len(jeu)):
        for j in range(len(jeu[0])):
            if jeu[i][j] == 2:
                return j, i  # x, y


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
                if powered:
                    print("ᗤ", end=" ")
                else:
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
    print("─" * int(longueur * 2 + 5), end="")
    print("╯")

    print("\n")


def pacmanMouvement(pacmanPosX, pacmanPosY, a, b):
    if pacmanPosX + a > len(jeu[0]) and jeu[pacmanPosY][0] == 0:
        jeu[pacmanPosY][0] = 2
        jeu[pacmanPosY][pacmanPosX] = 0
        return 0, pacmanPosY
    elif pacmanPosX + a < 0 and jeu[pacmanPosY][len(jeu[0])] == 0:
        jeu[pacmanPosY][len(jeu[0])] = 2
        jeu[pacmanPosY][pacmanPosX] = 0
        return len(jeu), pacmanPosY
    elif pacmanPosY + b > len(jeu) and jeu[0][pacmanPosX] == 0:
        jeu[0][pacmanPosX] = 2
        jeu[pacmanPosY][pacmanPosX] = 0
        return pacmanPosX, 0
    elif pacmanPosX + b < 0 and jeu[len(jeu)][pacmanPosX] == 0:
        jeu[len(jeu)][pacmanPosX] = 2
        jeu[pacmanPosY][pacmanPosX] = 0
        return pacmanPosX, len(jeu)
    elif jeu[pacmanPosY + b][pacmanPosX + a] == 0:
        jeu[pacmanPosY + b][pacmanPosX + a] = 2
        jeu[pacmanPosY][pacmanPosX] = 0


def UserInputGame(code):
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


def locateFantomes():
    fantomes = []
    for i in range(len(jeu)):
        for j in range(len(jeu[0])):
            if jeu[i][j] == 3:
                fantomes.append([i, j]) # y, x

    return fantomes


def fantomeMouvement():
    fantomes = locateFantomes()

    if len(fantomes) == 0:
        return True

    for fantome in fantomes:
        if jeu[fantome[0]][fantome[1]] == 2:
            return "died"


def cibleIAF():
    l=random.randint(0,len(jeu))
    c=random.randint(0,len(jeu[0]))
    if jeu[l][c]==0:
        return l,c
    else:
        return False


def IAF():
    cible=cibleIAF()
    

jeu = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
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

powered = False

while True:
    affiche_refresh(fps=8)
    if windows:
        code = UserInputWindows()
    else:
        code = userInputUnix()

    UserInputGame(code)
    win = fantomeMouvement()
    if win == True:
        clear()
        print(f"""{YELLOW}
__   __           __        __
\ \ / /__  _   _  \ \      / / (_)____
 \ V / _ \| | | |  \ \ /\ / /  | |  _ \ 
  | | (_) | |_| |   \ V  V /   | | | | |
  |_|\___/ \____|    \_/\_/    |_|_| |_|
{RESET}""")
        exit()

    elif win == "died":
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