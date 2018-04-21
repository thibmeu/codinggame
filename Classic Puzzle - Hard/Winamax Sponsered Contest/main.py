import sys
import math
import copy
from enum import Enum


class Arrow(Enum):
    LEFT = '<'
    RIGHT = '>'
    UP = '^'
    DOWN = 'v'


class Place(Enum):
    EMPTY = '.'
    HOLE = 'H'
    WATER = 'X'
    BALL = [str(i) for i in range(10)]
    ARROW = [i.value for i in Arrow]


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def validmove(self, arrow, dist):
        if arrow == Arrow.LEFT:
            return self.y >= dist
        elif arrow == Arrow.RIGHT:
            return self.y < width-dist
        elif arrow == Arrow.UP:
            return self.x >= dist
        elif arrow == Arrow.DOWN:
            return self.x < height-dist

    def move(self, arrow, dist):
        if arrow == Arrow.LEFT:
            self.y -= dist
        elif arrow == Arrow.RIGHT:
            self.y += dist
        elif arrow == Arrow.UP:
            self.x -= dist
        elif arrow == Arrow.DOWN:
            self.x += dist


def toplace(plan):
    r = [[None]*width for _ in range(height)]
    for row in range(height):
        for col in range(width):
            for p in Place:
                if plan[row][col] in p.value:
                    r[row][col] = p
    return r


def fillmove(plan, pos1, pos2):
    c = None
    line1, col1, line2, col2 = None, None, None, None
    if pos1.x < pos2.x:
        c = Arrow.DOWN.value
        line1, col1, line2, col2 = pos1.x, pos1.y, pos2.x+1, pos1.y+1
    elif pos2.x < pos1.x:
        c = Arrow.UP.value
        line1, col1, line2, col2 = pos2.x, pos1.y, pos1.x+1, pos1.y+1
    elif pos1.y < pos2.y:
        c = Arrow.RIGHT.value
        line1, col1, line2, col2 = pos1.x, pos1.y, pos1.x+1, pos2.y+1
    elif pos2.y < pos1.y:
        c = Arrow.LEFT.value
        line1, col1, line2, col2 = pos1.x, pos2.y, pos1.x+1, pos1.y+1

    save = []
    for i in range(line1, line2):
        for j in range(col1, col2):
            save.append(plan[i][j])
            plan[i][j] = c
    return save


def cleanmove(plan, pos1, pos2, save):
    line1, col1, line2, col2 = None, None, None, None
    if pos1.x < pos2.x:
        line1, col1, line2, col2 = pos1.x, pos1.y, pos2.x+1, pos1.y+1
    elif pos2.x < pos1.x:
        line1, col1, line2, col2 = pos2.x, pos1.y, pos1.x+1, pos1.y+1
    elif pos1.y < pos2.y:
        line1, col1, line2, col2 = pos1.x, pos1.y, pos1.x+1, pos2.y+1
    elif pos2.y < pos1.y:
        line1, col1, line2, col2 = pos1.x, pos2.y, pos1.x+1, pos1.y+1

    k = 0
    for i in range(line1, line2):
        for j in range(col1, col2):
            plan[i][j] = save[k]
            k += 1


def printplan(plan) :
    for r in plan:
        for v in r:
            print(v, end='', file=sys.stderr)
        print(file=sys.stderr)


def findpath(balls, plan):
    for i, ball in enumerate(balls):
        if plan[ball.x][ball.y] == 'H':
            if i == len(balls)-1:
                return True
            continue
        dist = int(plan[ball.x][ball.y])
        if dist == 0:
            if i == len(balls)-1:
                return True
            continue
        for a in Arrow:
            if ball.validmove(a, dist):
                sball = copy.deepcopy(ball)
                ball.move(a, dist)
                savecell = plan[ball.x][ball.y]
                save = fillmove(plan, sball, ball)
                if savecell not in 'H':
                    plan[ball.x][ball.y] = str(dist-1)
                else:
                    plan[ball.x][ball.y] = '0'
                printplan(plan)
                print("+++++++++", save[:], all([s not in 'H0123456789' for s in save[1:-1]]), file=sys.stderr)
                print(file=sys.stderr)
                if (savecell == 'H' or (savecell not in 'X^><v0123456789' and all([s not in 'H^><v0123456789' for s in save[1:-1]]))) and findpath(balls, plan):
                    print("-----------", file=sys.stderr)
                    return True
                else:
                    cleanmove(plan, sball, ball, save)
                    plan[ball.x][ball.y] = savecell
                    ball.x = sball.x
                    ball.y = sball.y
                    printplan(plan)
                    print(file=sys.stderr)

    return False

width, height = [int(i) for i in input().split()]
plan = [[None]*width for _ in range(height)]
balls = []
for i in range(height):
    for j, c in enumerate(input()):
        plan[i][j] = c
        if c in Place.BALL.value:
            balls.append(Point(i, j))

print('Plan de depart', file=sys.stderr)
printplan(plan)
print(file=sys.stderr)

findpath(balls, plan)

print(toplace(plan), file=sys.stderr)

for row in plan:
    for val in row:
        if val in 'XH0':
            val = '.'
        print(val, end='')
    print()
