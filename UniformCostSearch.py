from heapq import heappush, heappop
from itertools import combinations


def ucs(start, goal):
    info = {start: (0, None)}
    heap = [(0, start)]
    while len(heap) > 0:
        cost, v = heappop(heap)
        if v == goal:
            L = []
            x = goal
            while x != None:
                L.append(x)
                x = info[x][1]
            L.reverse()
            return L
        for weight, u in get_neighbors(v):
            if u not in info or cost + weight < info[u][0]:
                info[u] = (cost + weight, v)
                heappush(heap, (cost + weight, u))

    return []

def get_neighbors(v):
    N = []
    left, right, flashlight = v
    for x in left:
        new_left = left.replace(x, '')
        new_right = ''.join(sorted(right + x))
        N.append((int(x, 16), new_left, new_right, "R"))
    for x, y in combinations(left, 2):
        pass
    return N

'''
def get_neighbors(v):
    if v == 'A':
        return [(2, 'B'), (7, 'C')]
    elif v == "B":
        return [(1, "D"), (4, "C"), (2, "A")]
    elif v == "C":
        return [(4, "B"), (7, "A"), (6, "E")]
    elif v == "D":
        return [(1, "B"), (10, "E"), (8, "F")]
    elif v == "E":
        return [(4, "F"), (10, "D"), (5, "C")]
    else:
        return [(4, "E"), (8, "D")]
'''

print(ucs(("125a", "", 'L'), ('', '125a', 'R')))
