
words = [line.strip() for line in open("wordlist.txt")]
words = set(w for w in words if len(w) == 4)
alpha = 'abcdefghijklmnopqrstuvwxyz'


class Graph(dict):
    def add(self,v):
        self[v] = set()
    def add_edge(self,u,v):
        self[v].add(u)
        self[u].add(v)


def depth_limited_path(G, start, goal, limit):
    waiting = [(start, 0)]
    parent = {start:None}
    while len(waiting) > 0:
        w, current_depth = waiting.pop()
        for c in G[w]:
            if c == goal:
                path = [c]
                c = w
                while parent[c] != None:
                    path.append(c)
                    c = parent[c]
                path.append(c)
                path.reverse()
                return path

            if c not in parent and current_depth < limit:
                parent[c] = w
                waiting.append((c, current_depth + 1))
    return []


def iterative_deepening_path(G, start, goal, max_d):
    for i in range(max_d):
        result = depth_limited_path(G, start, goal, i)
        if result != []:
            return result

G = Graph()
for w in words:
    G.add(w)

for w in words:
    for i in range(len(w)):
        for a in alpha:
            n = w[:i] + a + w[i+1:]
            if n in words and n != w:
                G.add_edge(w,n)

print(iterative_deepening_path(G, 'wait','lift',100))