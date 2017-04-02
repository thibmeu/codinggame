import sys
import math
import copy

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

count = {}
nodes = {}

n = int(input())  # the number of relationships of influence
for i in range(n):
    # x: a relationship of influence between two people (x influences y)
    x, y = [int(j) for j in input().split()]
    if x not in count:
        count[x] = True
    count[x] = False
    if y not in count:
        count[y] = True

    if y not in nodes:
        nodes[y] = []
    nodes[y].append(x)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

leaves = []
for i in count:
    if count[i]:
        leaves.append((i, 1))

leave, depth = None, None
while leaves:
    leave, depth = leaves.pop(0)
    if leave in nodes:
        for i in nodes[leave]:
            leaves.append((i, depth + 1))

# The number of people involved in the longest succession of influences
print(depth)
