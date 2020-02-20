from random import choice, randint, random
from math import exp


def hill_climbing(start, h):
    v = start
    while h(v) != 0:
        N = sorted([(h(n), n) for n in get_neighbors(v)])
        best = N[0][0]
        v = choice([n[1] for n in N if n[0] == best])
    return v


def anneal(start, h):
    temp = 10
    num_iter = 100
    stop_temp = 1

    v = start

    while h(v) != stop_temp and h(v) != 0:
        row = randint(0, len(v) - 1)
        col = randint(0, len(v) - 1)
        n = v[:row] + (col, ) + v[row+1:]
        if h(n) < h(v):
            v = n
        else:
            if exp((h(v)-h(n))/temp) > random():
                v = n
        temp *= .99
    return v


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


t = (0, ) * 4
display(t)
print()
display(anneal(t, num_attacking))
