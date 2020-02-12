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


def get_neighbors(v):
    z = v.index(0)
    N = []
    if z >= 3:
        N.append(v[:z - 3] + (v[z],) + v[z - 2: z] + (v[z - 3],) + v[z + 1:])
    if z <= 5:
        N.append(v[:z] + (v[z + 3],) + v[z + 1:z + 3] + (v[z],) + v[z + 4:])
    if z % 3 != 0:
        N.append(v[:z-1] + (v[z], v[z-1]) + v[z + 1:])
    if z % 3 != 2:
        N.append(v[:z] + (v[z + 1], v[z])+v[z + 2])
    return N


start = (5, 8, 2, 4, 0, 6, 3, 1, 7)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

print(astar(start, goal, get_neighbors, h1))