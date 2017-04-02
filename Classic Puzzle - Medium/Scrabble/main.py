import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

score = {key: 1 for key in ['e', 'a', 'i', 'o', 'n', 'r', 't', 'l', 's', 'u']}
score.update({key: 2 for key in ['d', 'g']})
score.update({key: 3 for key in ['b', 'c', 'm', 'p']})
score.update({key: 4 for key in ['f', 'h', 'v', 'w', 'y']})
score.update({key: 5 for key in ['k']})
score.update({key: 8 for key in ['j', 'x']})
score.update({key: 10 for key in ['q', 'z']})

def getPoints(w):
    s = 0
    for c in w:
        s += score[c]
    return s

#Works because only 7 letters
def canMake(ref, word):
    i = 0
    for l in word:
        while i < len(ref) and l != ref[i]:
            i += 1
        if i >= len(ref):
            return False
        i += 1
    return True

words = []
n = int(input())
for i in range(n):
    w = input()
    if len(w) > 7:
        continue
    words.append((''.join(sorted(w)), w))
letters = ''.join(sorted(input()))

wordMax, scoreMax = "", 0
for sortedWord, word in words:
    if canMake(letters, sortedWord):
        p = getPoints(word)
        if scoreMax < p:
            wordMax = word
            scoreMax = p

print(wordMax)
