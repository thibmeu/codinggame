import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

r = int(input())
l = int(input())

seq = [r]
for iLine in range(l-1):
    curSeq = []
    count, prec = 0, 0
    for i in seq:
        if count != 0 and i != prec:
            curSeq.extend([count, prec])
            count = 0
        count += 1
        prec = i
    seq = curSeq + [count, prec]

s = ""
for i in seq:
    s += str(i) + " "

print(s[:-1])
