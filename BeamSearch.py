from random import choice, randint, random
from math import exp


def beam(start, h, width):
    waiting = [start]
    found = {start}
    while waiting:
        w = waiting.pop(0)
        if h(w) == 0:
            return w
        N = sorted([(h(n), n) for n in get_neighbors(w)])[:width]
        for _, x in N:
            if x not in found:
                waiting.append(x)
                found.add(x)
    return []


def get_neighbors(t):
    N = []
    for i in range(len(t)):
        for j in range(len(t)):
            c = list(t)[:]
            c[i] = j
            if c != list(t):
                N.append(tuple(c))
    return N


def num_attacking(t):
    vertical = len(t) - len(set(t))
    coords = list(enumerate(t))
    diagonal = 0
    for r in range(len(t) - 1):
        c = t[r]
        rc = c + 1
        lc = c - 1
        for nr in range(r + 1, len(t)):
            if (nr, rc) in coords or (nr, lc) in coords:
                diagonal += 1
            rc += 1
            lc -= 1
    return vertical + diagonal


def display(t):
    coords = list(enumerate(t))
    for i in range(len(t)):
        for j in range(len(t)):
            if (i, j) in coords:
                print(" Q", end=" ")
            else:
                print(" -", end=" ")
        print()


t = (0, ) * 8

ans = beam(t, num_attacking, 3)


display(t)
print()
display(ans)
