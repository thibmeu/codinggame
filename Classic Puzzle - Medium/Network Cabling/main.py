import sys
import math
from statistics import median

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

min, max = pow(2, 30), -1*pow(2, 30)
yPos = []
n = int(input())
for i in range(n):
    x, y = [int(j) for j in input().split()]
    yPos.append(y)
    if min > x:
        min = x
    if max < x:
        max = x
med = int(median(yPos))

s = max-min
for y in yPos:
    s += abs(y-med)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(s)
