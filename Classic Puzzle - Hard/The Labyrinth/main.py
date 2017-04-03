import sys
import copy

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# r: number of rows.
# c: number of columns.
# a: number of rounds between the time the alarm countdown is activated and the time the alarm goes off.
height, width, alarm = [int(i) for i in input().split()]


def inGrid(pos):
    return pos[1] >= 0 and pos[1] < width and pos[0] >= 0 and pos[0] < height

path = None


def distanceOk(plan, posInit, posAlarm, countdown):
    pos = [(posInit, 0)]
    grid = copy.deepcopy(plan)
    grid[posInit[1]][posInit[0]] = 0
    while pos:
        (y, x), dist = pos.pop(0)
        if not inGrid((y, x)):
            continue
        if grid[y][x] in {'.', 'C'} or (type(grid[y][x]) is int and grid[y][x] > dist):
            grid[y][x] = dist
            pos.extend([((y + 1, x), dist + 1), ((y - 1, x), dist + 1), ((y, x + 1), dist + 1), ((y, x - 1), dist + 1)])

    path = [posAlarm]
    while path[0] != posInit:
        y, x = path[0]
        dist = grid[y][x] if type(grid[y][x]) is int else -1
        if inGrid((y+1, x)) and grid[y+1][x] == dist-1:
            path = [(y+1, x)] + path
        elif inGrid((y+1, x)) and grid[y-1][x] == dist-1:
            path = [(y-1, x)] + path
        elif inGrid((y, x+1)) and grid[y][x+1] == dist-1:
            path = [(y, x+1)] + path
        elif inGrid((y, x-1)) and grid[y][x-1] == dist-1:
            path = [(y, x-1)] + path

    return len(path)-1 <= countdown

# game loop
#
isAlarm = False
trouvee = False
firstX, firstY = None, None
while True:
    # kr: row where Kirk is located.
    # kc: column where Kirk is located.
    kr, kc = [int(i) for i in input().split()]
    print(kr, kc, file=sys.stderr)

    if not firstX:
        firstX, firstY = kc, kr

    plan = []
    for i in range(height):
        print("-", file=sys.stderr)
        if trouvee and i == height-1:
            continue

        p = input()
        print("+", file=sys.stderr)
        plan.append(list(p))  # C of the characters in '#.TC?' (i.e. one line of the ASCII maze).
        print(''.join(plan[-1]), file=sys.stderr)

    if plan[kr][kc] == 'C':
        isAlarm = True

    print(isAlarm, file=sys.stderr)

    dejaVu = [[False]*width for _ in range(height)]
    pos = [(kr, kc)]
    if not isAlarm:
        print("Salle de controle non atteinte", file=sys.stderr)
        y, x = None, None
        while pos:
            y, x = pos.pop(0)
            if not inGrid((y, x)):
                continue
            if plan[y][x] in {'.', 'T'} and not dejaVu[y][x]:
                dejaVu[y][x] = True
                pos.extend([(y+1, x), (y-1, x), (y, x+1), (y, x-1)])
            elif plan[y][x] == '?' or (plan[y][x] == 'C' and distanceOk(plan, (firstY, firstX), (y, x), alarm)):
                print(x, y, file=sys.stderr)
                break
        dy, dx = y-kr, x-kc
        print("dy: ", dy, ", dx: ", dx, file=sys.stderr)
        if (abs(dx) < abs(dy) and dx != 0) or dy == 0:
            if dx < 0:
                print("LEFT")
            else:
                print("RIGHT")
        else:
            if dy < 0:
                print("UP")
            else:
                print("DOWN")
    else:
        print("On court pour revenir au point de depart", file=sys.stderr)
        iPath = path.index((kr,kc))
        y, x = path[iPath-1]
        dy, dx = y - kr, x - kc
        if abs(dx) < abs(dy):
            if dx < 0:
                print("LEFT")
            else:
                print("RIGHT")
        else:
            if dy < 0:
                print("UP")
            else:
                print("DOWN")
