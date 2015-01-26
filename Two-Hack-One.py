import string
import sys
alphaMap = dict.fromkeys(string.ascii_lowercase, 0)
isCorrectMap = []


def fillCorrectMatrix():
    file = open('wordScores.txt', 'r')
    line = file.readline()
    while line != '':
        temp = line.split('')
        isCorrectMap[temp[0]] = temp[1]
        line = file.readline()

def sumAlpha(list):
    sum = 0
    for i in list:
        sum = alphaMap[i]
    return sum

def isCorrect():
    vowelList     = []
    consonantList = []
    for key, value in isCorrectMatrix:
        for alpha in key:
            if alpha = 'a' or alpha = 'e' or alpha = 'i' or alpha = 'o' or alpha = 'u':
                vowelList.append(alpha)
            else
                consonantList.append(alpha)
        if sumAlpha(vowelList) * sumAlpha(consonantList) != value:
            return False
    return True


def findAnswer(n):
    for a in range(1,27):
        for b in range(1,27):
            for c in range(1,27):
                for d in range(1,27):
                    for e in range(1,27):
                        for f in range(1,27):
                            for g in range(1,27):
                                for h in range(1,27):
                                    for i in range(1,27):
                                        for j in range(1,27):
                                            for k in range(1,27):
                                                for l in range(1,27):
                                                    for m in range(1,27):
                                                        for n in range(1,27):
                                                            for o in range(1,27):
                                                                for p in range(1,27):
                                                                    for q in range(1,27):
                                                                        for r in range(1,27):
                                                                            for s in range(1,27):
                                                                                for t in range(1,27):
                                                                                    for u in range(1,27):
                                                                                        for v in range(1,27):
                                                                                            for w in range(1,27):
                                                                                                for x in range(1,27):
                                                                                                    for y in range(1,27):
                                                                                                        for z in range(1,27):
                                                                                                            alphaMap['a'] = a
                                                                                                            alphaMap['b'] = b
                                                                                                            alphaMap['c'] = c
                                                                                                            alphaMap['d'] = d
                                                                                                            alphaMap['e'] = e
                                                                                                            alphaMap['f'] = f
                                                                                                            alphaMap['g'] = g
                                                                                                            alphaMap['h'] = h
                                                                                                            alphaMap['i'] = i
                                                                                                            alphaMap['j'] = j
                                                                                                            alphaMap['k'] = k
                                                                                                            alphaMap['l'] = l
                                                                                                            alphaMap['m'] = m
                                                                                                            alphaMap['n'] = n
                                                                                                            alphaMap['o'] = o
                                                                                                            alphaMap['p'] = p
                                                                                                            alphaMap['q'] = q
                                                                                                            alphaMap['r'] = r
                                                                                                            alphaMap['s'] = s
                                                                                                            alphaMap['t'] = t
                                                                                                            alphaMap['u'] = u
                                                                                                            alphaMap['v'] = v
                                                                                                            alphaMap['w'] = w
                                                                                                            alphaMap['x'] = x
                                                                                                            alphaMap['y'] = y
                                                                                                            alphaMap['z'] = z
                                                                                                            if isCorrect():
                                                                                                                for key, value in alphaMap:
                                                                                                                    print(key, ' ', value)
                                                                                                                    sys.exit()
print('No solution possible')
