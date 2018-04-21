import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
c = int(input())

oods = []
for i in range(n):
    oods.append(int(input()))
oods = sorted(oods)

cannotOods = []
sumCannot = 0
while oods:
    sumOod = oods.pop(0)
    max = sumOod*(len(oods)+1) + sumCannot
    if max > c:
        oods = [sumOod] + oods
        break
    cannotOods.append(sumOod)
    sumCannot += sumOod

if not oods:
    print("IMPOSSIBLE")
else:
    for sum in cannotOods:
        print(sum)
    reste = c - sumCannot
    bonus = reste%len(oods)
    d = reste//len(oods)
    for i in range(len(oods)):
        if i >= len(oods)-bonus:
            print(d+1)
        else:
            print(d)

