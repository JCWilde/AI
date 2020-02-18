from heapq import heappush, heappop
from random import choice


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


def get_neighbors(v):
    z = v.index(0)
    N = []
    if z >= 3:
        N.append((1, v[:z-3]+(v[z],)+v[z-2:z]+(v[z-3],)+v[z+1:]))
    if z <= 5:
        N.append((1, v[:z]+(v[z+3],)+v[z+1:z+3]+(v[z],)+v[z+4:]))
    if z % 3 != 0:
        N.append((1, v[:z-1]+(v[z],v[z-1])+v[z+1:]))
    if z % 3 != 2:
        N.append((1, v[:z]+(v[z+1],v[z])+v[z+2:]))
    return N


def num_tiles_out_of_place(v, goal):
    return sum(1 for i in range(len(v)) if v[i] != (i + 1) % 9)


def manhattan(v, goal):
    res = 0
    for i in range(len(v)):
        x = v[i] % 3
        if v[i] == 0:
            x = 9
        cur_row = i // 3
        cur_col = i % 3
        prop_row = (x-1) // 3
        prop_col = (x-1) % 3
        res += abs(prop_row - cur_row) + abs(prop_col - cur_col)
    return res


goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

start = goal[:]
for i in range(2000):
    start = choice(get_neighbors(start))[1]

print(len(ucs(start, goal, get_neighbors)))

print(len(astar(start, goal, get_neighbors, manhattan)))
print(len(astar(start, goal, get_neighbors, num_tiles_out_of_place)))

print(len(greedy_best(start, goal, get_neighbors, manhattan)))
print(len(greedy_best(start, goal, get_neighbors, num_tiles_out_of_place)))
