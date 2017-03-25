import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: number of columns.
# h: number of rows.
w, h = [int(i) for i in input().split()]
carte = [[] for _ in range(h)]
for i in range(h):
    line = input()  # represents a line in the grid and contains W integers. Each integer represents one room of a given type.
    carte[i] = [int(i) for i in line.split()]
ex = int(input())  # the coordinate along the X axis of the exit (not useful for this first mission, but must be read).

# game loop
while True:
    xi, yi, pos = input().split()
    xi = int(xi)
    yi = int(yi)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    sortie = carte[yi][xi]
    if sortie == 1:
        yi += 1
    elif sortie == 2:
        xi += 1 if pos == 'LEFT' else -1
    elif sortie == 3:
        yi += 1
    elif sortie == 4:
        if pos == 'TOP':
            xi -= 1
        else:
            yi += 1
    elif sortie == 5:
        if pos == 'TOP':
            xi += 1
        else:
            yi += 1
    elif sortie == 6:
        xi += 1 if pos == 'LEFT' else -1
    elif sortie == 7:
        yi += 1
    elif sortie == 8:
        yi += 1
    elif sortie == 9:
        yi += 1
    elif sortie == 10:
        xi -= 1
    elif sortie == 11:
        xi += 1
    elif sortie == 12:
        yi += 1
    elif sortie == 13:
        yi += 1

    # One line containing the X Y coordinates of the room in which you believe Indy will be on the next turn.
    print(xi, yi)
