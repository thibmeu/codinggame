import sys
import math
import copy

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

count = {}
nodes = {}

n = int(input())  # the number of adjacency relations
print(n, file=sys.stderr)
for i in range(n):
    # xi: the ID of a person which is adjacent to yi
    # yi: the ID of a person which is adjacent to xi
    xi, yi = [int(j) for j in input().split()]
    if xi not in count:
        count[xi] = 0
    if yi not in count:
        count[yi] = 0
    count[xi] += 1
    count[yi] += 1
    if xi not in nodes:
        nodes[xi] = []
    if yi not in nodes:
        nodes[yi] = []
    nodes[xi].append(yi)
    nodes[yi].append(xi)
    print(xi, yi, file=sys.stderr)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

leaves = []
for i in count:
    if count[i] == 1:
        leaves.append((i, 0))

burningTree = copy.deepcopy(nodes)
leave, depth = None, None
while leaves:
    leave, depth = leaves.pop(0)
    if not (len(burningTree[leave]) == 1):
        continue

    for i in burningTree[leave]:
        leaves.append((i, depth + 1))
        burningTree[leave].remove(i)
        burningTree[i].remove(leave)

# The minimal amount of steps required to completely propagate the advertisement
print(leave, file=sys.stderr)
print(depth)