import sys
import copy


def inGrid(p):
    return 0 <= p[1] < width and 0 <= p[0] < height


def distanceOk(plan, posInit, posAlarm, countdown):
    global path
    pos = [(posInit, 0)]
    grid = copy.deepcopy(plan)
    while pos:
        (y, x), dist = pos.pop(0)
        if not inGrid((y, x)):
            continue
        if grid[y][x] in {'T', '.', 'C'} or (type(grid[y][x]) is int and grid[y][x] > dist):
            grid[y][x] = dist
            pos.extend([((y + 1, x), dist + 1), ((y - 1, x), dist + 1), ((y, x + 1), dist + 1), ((y, x - 1), dist + 1)])

    path = [posAlarm]
    while path[0] != posInit:
        y, x = path[0]
        dist = grid[y][x] if type(grid[y][x]) is int else -1
        if inGrid((y + 1, x)) and grid[y + 1][x] == dist - 1:
            path = [(y + 1, x)] + path
        elif inGrid((y + 1, x)) and grid[y - 1][x] == dist - 1:
            path = [(y - 1, x)] + path
        elif inGrid((y, x + 1)) and grid[y][x + 1] == dist - 1:
            path = [(y, x + 1)] + path
        elif inGrid((y, x - 1)) and grid[y][x - 1] == dist - 1:
            path = [(y, x - 1)] + path

    return len(path) - 1 <= countdown


height, width, alarm = [int(i) for i in input().split()]
path = None

# game loop
#
isAlarm = False
firstX, firstY = None, None
while True:
    # kr: row where Kirk is located.
    # kc: column where Kirk is located.
    kr, kc = [int(i) for i in input().split()]
    if not firstX:
        firstX, firstY = kc, kr

    plan = []
    isC = False
    for i in range(height):
        plan.append(list(input()))

    if plan[kr][kc] == 'C':
        isAlarm = True

    dejaVu = [[False]*width for _ in range(height)]
    if not isAlarm:
        pos = [(kr+1, kc, "DOWN"), (kr-1, kc, "UP"), (kr, kc+1, "RIGHT"), (kr, kc-1, "LEFT")]
        y, x, direc = None, None, None
        while pos:
            y, x, direc = pos.pop(0)
            if not inGrid((y, x)):
                continue
            if plan[y][x] in {'.', 'T'} and not dejaVu[y][x]:
                dejaVu[y][x] = True
                pos.extend([(y+1, x, direc), (y-1, x, direc), (y, x+1, direc), (y, x-1, direc)])
            elif plan[y][x] == '?' or (plan[y][x] == 'C' and distanceOk(plan, (firstY, firstX), (y, x), alarm)):
                break
        print(direc)
    else:
        iPath = path.index((kr, kc))
        y, x = path[iPath-1]
        if abs(x - kc) > 0:
            if x < kc:
                print("LEFT")
            else:
                print("RIGHT")
        else:
            if y < kr:
                print("UP")
            else:
                print("DOWN")
