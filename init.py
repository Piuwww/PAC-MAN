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


def pacmanMouvement(pacmanPosX, pacmanPosY, a, b):
    if pacmanPosX + a > 18 and jeu[pacmanPosY][0] == 0:
        jeu[pacmanPosY][0] = 2
        jeu[pacmanPosY][pacmanPosX] = 0
        return 0, pacmanPosY
    elif pacmanPosX + a < 0 and jeu[pacmanPosY][18] == 0:
        jeu[pacmanPosY][18] = 2
        jeu[pacmanPosY][pacmanPosX] = 0
        return 13, pacmanPosY
    elif pacmanPosY + b > 13 and jeu[0][pacmanPosX] == 0:
        jeu[0][pacmanPosX] = 2
        jeu[pacmanPosY][pacmanPosX] = 0
        return pacmanPosX, 0
    elif pacmanPosX + b < 0 and jeu[13][pacmanPosX] == 0:
        jeu[13][pacmanPosX] = 2
        jeu[pacmanPosY][pacmanPosX] = 0
        return pacmanPosX, 13
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

    return UserInputGame(ord(character))


def UserInputWindows():
    if msvcrt.kbhit():
        character = msvcrt.getch()
        return UserInputGame(ord(character))


# init
jeu = [
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
]

while True:
    affiche_refresh(fps=60)
    if windows:
        UserInputWindows()
    else:
        userInputUnix()
