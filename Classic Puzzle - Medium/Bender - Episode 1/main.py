import sys

directions = ['S', 'E', 'N', 'W']
printDirections = ['SOUTH', 'EAST', 'NORTH', 'WEST']
direction = 0
nBreaker = 0
isBreaker = False
isInvert = False
isObstacle = False
sprint = ''


def avancer(direction):
    global isObstacle, sprint
    sprint += printDirections[direction] + '\n'
    isObstacle = False


l, c = [int(i) for i in input().split()]
plan = []
for i in range(l):
    p = input()
    print(p, file=sys.stderr)
    plan.append(list(p))

pos = []
teleporters = []
for i in range(l):
    for j in range(c):
        if plan[i][j] == '@':
            pos = [(i, j)]
        elif plan[i][j] == 'T':
            teleporters.append((i, j))

memory = [[[(None, None, None)]*len(directions) for j in range(c)] for i in range(l)]

while pos:
    x, y = pos.pop(0)
    if memory[x][y][direction] == (isBreaker, isInvert, nBreaker) and not isObstacle:
        sprint = 'LOOP'
        break
    memory[x][y][direction] = (isBreaker, isInvert, nBreaker)

    nx, ny = x, y
    if direction == 0:
        nx += 1
    elif direction == 1:
        ny += 1
    elif direction == 2:
        nx -= 1
    elif direction == 3:
        ny -= 1

    ncase = plan[nx][ny] if 0 <= nx < l and 0 <= ny <= c else '#'

    if ncase in {'#', 'X'}:
        if isBreaker and ncase == 'X':
            nBreaker += 1
            plan[nx][ny] = ' '
            avancer(direction)
        else:
            if not isObstacle:
                direction = 3 if isInvert else 0
                isObstacle = True
            else:
                direction = (direction + (-1 if isInvert else 1)) % 4
            nx, ny = x, y
    elif ncase in directions:
        avancer(direction)
        direction = directions.index(ncase)
    elif ncase == 'B':
        isBreaker = not isBreaker
        avancer(direction)
    elif ncase == 'I':
        isInvert = not isInvert
        avancer(direction)
    elif ncase == 'T':
        avancer(direction)
        nx, ny = teleporters[0] if teleporters[0] != (nx, ny) else teleporters[1]
    elif ncase == '$':
        avancer(direction)
        break
    else:
        avancer(direction)
    pos.append((nx, ny))

print(sprint)
