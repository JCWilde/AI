from heapq import heappush, heappop

def ucs(start, goal, get_neighbors):
    info = {start: (0, None)}
    heap = [(0, start)]
    while len(heap) > 0:
        pri, v = heappop(heap)
        if v == goal:
            L = []
            x = v
            while x != None:
                L.append(x)
                x = info[x][1]
            L.reverse()
            return L

        cost = info[v][0]
        for weight, u in get_neighbors(v):
            if u not in info or weight + cost < info[u][0]:
                info[u] = (weight+cost, v)
                heappush(heap, (weight+cost, u))

    return []

def astar(start, goal, get_neighbors, heuristic):
    info = {start: (0, None)}
    heap = [(0, start)]
    while len(heap) > 0:
        pri, v = heappop(heap)
        if v == goal:
            L = []
            x = v
            while x != None:
                L.append(x)
                x = info[x][1]
            L.reverse()
            return L

        cost = info[v][0]
        for weight, u in get_neighbors(v):
            if u not in info or weight + cost < info[u][0]:
                info[u] = (weight+cost, v)
                heappush(heap, (weight+cost+heuristic(u,goal), u))

    return []

def greedy_best(start, goal, get_neighbors, heuristic):
    info = {start: None} # just store parent info
    heap = [(0, start)]
    while len(heap) > 0:
        pri, v = heappop(heap)
        if v == goal:
            L = []
            x = v
            while x != None:
                L.append(x)
                x = info[x]
            L.reverse()
            return L

        for weight, u in get_neighbors(v):
            if u not in info:
                info[u] = v
                heappush(heap, (heuristic(u, goal), u))

    return []


board = """
000*0000000000000000
000*0000000000000000
000*0000000000000000
000*0000000000000000
000*0000000000000000
000*0000000000000000
00000000000000000000
000*0000000000000000
000*0000000000000000
000*0000000000000000
000*0000000000000000
000***0***0000000000
000000000*0000000000
000000000*0000000000
000000000**0*0000000
000000000*00*0000000
000000000*0**00**000
000000000*00*00*0000
000000000**0****0***
000000000*0000000000"""

from random import *
seed(12345)
s = list(('0'*280) + ("*"*120))
shuffle(s)
s[0] = '0'
s[len(s) - 1] = '0'
board = [s[i:i+20] for i in range(0, 400, 20)]

#board = [list(x) for x in board[1:].split('\n')]


def get_neighbors1(v):
    r, c = v
    N = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
    return [(1, (a, b)) for a, b in N if 0 <= a < 20 and 0 <= b < 20 and board[a][b] == '0']


def get_neighbors2(v):
    r, c = v
    N = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1), (r + 1, c - 1), (r + 1, c + 1), (r - 1, c - 1), (r - 1, c + 1)]
    return [(1, (a, b)) for a, b in N if 0 <= a < 20 and 0 <= b < 20 and board[a][b] == '0']


def manhattan(v, goal):
    r, c = v
    rg, cg = goal
    return abs(rg - r) + abs(cg - c)


def euclidean(v, goal):
    r, c = v
    rg, cg = goal
    return ((rg - r) ** 2 + (cg - c) ** 2) ** .5


# L = ucs((0,0), (19,19), get_neighbors1)
# L = astar((0,0), (19,19), get_neighbors1, manhattan)
L = astar((0,0), (19,19), get_neighbors2, euclidean)
#L = astar((0, 0), (19, 19), get_neighbors2, manhattan)

for i in range(len(L)):
    r, c = L[i]
    board[r][c] = str(i)

'''
for i in range(len(ORDER)):
    r, c = ORDER[i]
    board[r][c] = str(i + 1)
'''
for i in range(len(board)):
    for j in range(len(board[i])):
        print('{:>3s} '.format(board[i][j]), end='')
    print()