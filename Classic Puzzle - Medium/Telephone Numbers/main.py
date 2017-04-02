import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
tree = {}
s = 0
for i in range(n):
    telephone = input()
    seq = tree
    for iChar in range(len(telephone)):
        if not telephone[iChar] in seq:
            seq[telephone[iChar]] = {}
            s += 1
        seq = seq[telephone[iChar]]


# The number of elements (referencing a number) stored in the structure.
print(s)
