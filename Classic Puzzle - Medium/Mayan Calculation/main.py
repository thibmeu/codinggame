import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

base = 20

l, h = [int(i) for i in input().split()]
decToMaya = dict.fromkeys(range(base), "")
for i in range(h):
    numeral = input()
    for i in range(base):
        decToMaya[i] += numeral[i*l:((i+1)*l)]

mayaToDec = dict((decToMaya[k],k) for k in decToMaya)
s1 = int(input())
n1 = 0
for i in range(s1//h):
    n = ""
    for _ in range(h):
        n += input()
    n1 += mayaToDec[n]*pow(base, s1//h-1-i)

s2 = int(input())
n2 = 0
for i in range(s2//h):
    n = ""
    for _ in range(h):
        n += input()
    n2 += mayaToDec[n]*pow(base, s2//h-1-i)
operation = input()

res = 0
if operation == "*":
    res = n1*n2
elif operation == "/":
    res = n1/n2
elif operation == "+":
    res = n1+n2
elif operation == "-":
    res = n1-n2

num = []
if res == 0:
    num = [0]
while res > 0:
    num = [res%base] + num
    res //= base

for i in num:
    for line in range(h):
        print(decToMaya[i][line*l:((line+1)*l)])