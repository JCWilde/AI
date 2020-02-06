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



# 1 min, 2 min, 5 min, 10 min.  The goal is to find the shortest crossing time.
def flashlight_neighbors(v):
    N = []
    left, right, flashlight = v

    if flashlight == 'L':
        for x in left:
            new_left = left.replace(x, '')
            new_right = ''.join(sorted(right + x))
            N.append((int(x, 16), (new_left, new_right, 'R')))
        for x, y in combinations(left, 2):
            new_left = left.replace(x, '').replace(y, '')
            new_right = ''.join(sorted(right + x + y))
            N.append((max(int(x, 16), int(y, 16)), (new_left, new_right, 'R')))
    else:
        for x in right:
            new_right = right.replace(x, '')
            new_left = ''.join(sorted(left + x))
            N.append((int(x, 16), (new_left, new_right, 'L')))
        for x, y in combinations(right, 2):
            new_right = right.replace(x, '').replace(y, '')
            new_left = ''.join(sorted(left + x + y))
            N.append((max(int(x, 16), int(y, 16)), (new_left, new_right, 'R')))
    return N


res = ucs(("125a", "", 'L'), ('', '125a', 'R'), flashlight_neighbors)

for l, r, d in res:
    print('{} {} {}'.format(l, ('->', '<-')[d == "L"], r))
