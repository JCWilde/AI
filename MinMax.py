

class Digraph(dict):
    def add(self, v):
        self[v] = set()

    def add_edge(self, u, v):
        self[u].add(v)


MAX = 1
MIN = 2


def minmax(v, player):
    c = utility(v)
    if c != -1:
        return c
    results = [minmax(w, MAX if player == MIN else MIN) for w in G[v]]
    return max(results) if player == MAX else min(results)

def utility(v):
    util = {'e':6, 'f':3, 'g':2, 'h':4, 'l':3, 'm':7, 'j':1, 'k':5}
    return util[v] if v in util else -1


def choose_move(v, player):
    results = [(minmax(w, MAX if player == MIN else MIN), w) for w in G[v]]
    print(sorted(results, key = lambda x : x[1]))
    return max(results)[1] if player == MAX else min(results)[1]



V = "abcdefhjijklm"

E = "ab ac ad be bf bg ch ci dj dk il im"

G = Digraph()
for v in V:
    G.add(v)

for x, y in E.split():
    G.add_edge(x, y)

choose_move('a', MAX)
print(minmax('a', MAX))