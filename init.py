from os import system
from sys import platform
from time import sleep

windows = platform.startswith("win")

if windows:
    import msvcrt
    import math
    import heapq

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


def pacmanMouvement(pacmanPosX, pacmanPosY, a, b):
    if jeu[pacmanPosY + b][pacmanPosX + a] == 0:
        jeu[pacmanPosY + b][pacmanPosX + a] = 2
        jeu[pacmanPosY][pacmanPosX] = 0
    elif (
        jeu[pacmanPosY + b][pacmanPosX + a] == 3
        or jeu[pacmanPosY + b][pacmanPosX + a] == 4
    ):
        jeu[pacmanPosY][pacmanPosX] = jeu[pacmanPosY + b][pacmanPosX + a]


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
                fantomes.append([i, j])  # y, x

    return fantomes


def fantomeMouvement():
    fantomes = locateFantomes()

    if len(fantomes) == 0:
        return True

    for fantome in fantomes:
        if jeu[fantome[0]][fantome[1]] == 2 and PacmanPowered:
            return False
        elif jeu[fantome[0]][fantome[1]] == 2 and not PacmanPowered:
            jeu[fantome[0]][fantome[1]] = 0
            return None

def IAF():
    # Define the Cell class


    class Cell:
        def __init__(self):
        # Parent cell's row index
            self.parent_i = 0
        # Parent cell's column index
            self.parent_j = 0
    # Total cost of the cell (g + h)
            self.f = float('inf')
        # Cost from start to this cell
            self.g = float('inf')
        # Heuristic cost from this cell to destination
            self.h = 0


    # Define the size of the jeu
    ROW = len(jeu)
    COL = len(jeu[0])

    # Check if a cell is valid (within the jeu)


    def is_valid(row, col):
        return (row >= 0) and (row < ROW) and (col >= 0) and (col < COL)

    # Check if a cell is unblocked


    def is_unblocked(jeu, row, col):
        return jeu[row][col] == 1

    # Check if a cell is the destination


    def is_destination(row, col, dest):
        return row == dest[0] and col == dest[1]

    # Calculate the heuristic value of a cell (Euclidean distance to destination)


    def calculate_h_value(row, col, dest):
        return ((row - dest[0]) ** 2 + (col - dest[1]) ** 2) ** 0.5

    # Trace the path from source to destination


    def trace_path(cell_details, dest):
        print("The Path is ")
        path = []
        row = dest[0]
        col = dest[1]

        # Trace the path from destination to source using parent cells
        while not (cell_details[row][col].parent_i == row and cell_details[row][col].parent_j == col):
            path.append((row, col))
            temp_row = cell_details[row][col].parent_i
            temp_col = cell_details[row][col].parent_j
            row = temp_row
            col = temp_col

        # Add the source cell to the path
        path.append((row, col))
        # Reverse the path to get the path from source to destination
        path.reverse()

        # Print the path
        for i in path:
            print("->", i, end=" ")
        print()

    # Implement the A* search algorithm


    def a_star_search(jeu, src, dest):
        # Check if the source and destination are valid
        if not is_valid(src[0], src[1]) or not is_valid(dest[0], dest[1]):
            print("Source or destination is invalid")
            return

        # Check if the source and destination are unblocked
        if not is_unblocked(jeu, src[0], src[1]) or not is_unblocked(jeu, dest[0], dest[1]):
            print("Source or the destination is blocked")
            return

        # Check if we are already at the destination
        if is_destination(src[0], src[1], dest):
            print("We are already at the destination")
            return

        # Initialize the closed list (visited cells)
        closed_list = [[False for _ in range(COL)] for _ in range(ROW)]
        # Initialize the details of each cell
        cell_details = [[Cell() for _ in range(COL)] for _ in range(ROW)]

        # Initialize the start cell details
        i = src[0]
        j = src[1]
        cell_details[i][j].f = 0
        cell_details[i][j].g = 0
        cell_details[i][j].h = 0
        cell_details[i][j].parent_i = i
        cell_details[i][j].parent_j = j

        # Initialize the open list (cells to be visited) with the start cell
        open_list = []
        heapq.heappush(open_list, (0.0, i, j))

        # Initialize the flag for whether destination is found
        found_dest = False

        # Main loop of A* search algorithm
        while len(open_list) > 0:
            # Pop the cell with the smallest f value from the open list
            p = heapq.heappop(open_list)

            # Mark the cell as visited
            i = p[1]
            j = p[2]
            closed_list[i][j] = True

            # For each direction, check the successors
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0),
                        (1, 1), (1, -1), (-1, 1), (-1, -1)]
            for dir in directions:
                new_i = i + dir[0]
                new_j = j + dir[1]

                # If the successor is valid, unblocked, and not visited
                if is_valid(new_i, new_j) and is_unblocked(jeu, new_i, new_j) and not closed_list[new_i][new_j]:
                    # If the successor is the destination
                    if is_destination(new_i, new_j, dest):
                        # Set the parent of the destination cell
                        cell_details[new_i][new_j].parent_i = i
                        cell_details[new_i][new_j].parent_j = j
                        print("The destination cell is found")
                        # Trace and print the path from source to destination
                        trace_path(cell_details, dest)
                        found_dest = True
                        return
                    else:
                        # Calculate the new f, g, and h values
                        g_new = cell_details[i][j].g + 1.0
                        h_new = calculate_h_value(new_i, new_j, dest)
                        f_new = g_new + h_new

                        # If the cell is not in the open list or the new f value is smaller
                        if cell_details[new_i][new_j].f == float('inf') or cell_details[new_i][new_j].f > f_new:
                            # Add the cell to the open list
                            heapq.heappush(open_list, (f_new, new_i, new_j))
                            # Update the cell details
                            cell_details[new_i][new_j].f = f_new
                            cell_details[new_i][new_j].g = g_new
                            cell_details[new_i][new_j].h = h_new
                            cell_details[new_i][new_j].parent_i = i
                            cell_details[new_i][new_j].parent_j = j

        # If the destination is not found after visiting all cells
        if not found_dest:
            print("Failed to find the destination cell")

    # Driver Code


    def main():
        

        # Define the source and destination
        src = [8, 0]
        dest = [0, 0]

        # Run the A* search algorithm
        a_star_search(jeu, src, dest)


    if __name__ == "__main__":
        main()


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

PacmanPowered = False

while True:
    affiche_refresh(fps=8)
    if windows:
        code = UserInputWindows()
    else:
        code = userInputUnix()

    UserInputGame(code)
    win = fantomeMouvement()
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
