from heapq import heappop, heappush
from itertools import combinations


def ucs(start, goal, get_neighbors):
    info = {start: (0, None)}
    heap = [(0, start)]
    while heap:
        pri, v = heappop(heap)
        if v == goal:
            L = []
            x = goal
            while x != None:
                L.append(x)
                x = info[x][1]
            L.reverse()
            return L
        cost = info[v][0]
        for weight, u in get_neighbors(v):
            if u not in info or weight + cost < info[u][0]:
                info[u] = (weight + cost, v)
                heappush(heap, (weight + cost, u))
    return []


def aStar(start, goal, get_neighbors, heuristic):
    """

    :param start:
    :param goal:
    :param get_neighbors:
    :param heuristic:
    :return: Path

    A* algorithm uses a heuristic function as well as the cost considered so far
    """
    info = {start: (0, None)}
    heap = [(0, start)]
    while heap:
        pri, v = heappop(heap)
        if v == goal:
            L = []
            x = goal
            while x != None:
                L.append(x)
                x = info[x][1]
            L.reverse()
            return L
        cost = info[v][0]
        for weight, u in get_neighbors(v):
            if u not in info or weight + cost < info[u][0]:
                info[u] = (weight + cost, v)
                heappush(heap, (weight + cost + heuristic(u, goal), u))
    return []


def gbf(start, goal, get_neighbors, heuristic):
    """

    :param start:
    :param goal:
    :param get_neighbors:
    :param heuristic:
    :return: Path

    Greedy Best First removes everything that has to do with cost and only considers the heuristic function
    """
    info = {start: None}
    heap = [start]
    while heap:
        pri, v = heappop(heap)
        if v == goal:
            L = []
            x = goal
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
00000000000000000000
00000000000000000000
00000000000000000000
00000000000000000000
00000000000000000000
00000000000000000000
00000000000000000000
00000000000000000000
00000000000000000000
00000000000000000000
00000000000000000000
00000000000000000000
00000000000000000000
00000000000000000000
00000000000000000000
00000000000000000000
00000000000000000000
00000000000000000000
00000000000000000000
00000000000000000000"""

board = [list(x) for x in board[1:].split('\n')]


def get_neighbors1(v):
    r, c = v
    N = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
    return [(1, (a, b)) for a, b in N if 0 <= a < 20 and 0 <= b < 20 and board[a][b] == '0']


def get_neighbors2(v):
    r, c = v
    N = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1), (r + 1, c + 1), (r - 1, c + 1), (r + 1, c - 1), (r - 1, c - 1)]
    return [(1, (a, b)) for a, b in N if 0 <= a < 20 and 0 <= b < 20 and board[a][b] == '0']


def manhattan(v, goal):
    r, c = v
    rg, cg = goal
    return abs(rg - r) + abs(cg - c)


def euclidean(v, goal):
    r, c = v
    rg, cg = goal
    return ((rg - r) ** 2 + (cg - c) ** 2) ** .5


# L = ucs((0, 0), (19, 19), get_neighbors1)
L = gbf((0, 0), (19, 19), get_neighbors1, euclidean)

print(L)

for i in range(len(L)):
    r, c = L[i]
    board[r][c] = str(i)

for i in range(len(board)):
    for j in range(len(board[i])):
        print('{:3s} '.format(board[i][j]), end = "")
    print("")