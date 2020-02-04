words = [line.strip() for line in open("wordlist.txt")]
words = set(w for w in words if len(w) == 4)

class Graph(dict):
    def add(self,v):
        self[v] = set()
    def add_edge(self,u,v):
        self[v].add(u)
        self[u].add(v)

def bfs(G, start, goal):
    waiting = [start]
    found = {start}
    while len(waiting) > 0:
        w = waiting.pop(0) # examine first found
        for c in G[w]:
            if c == goal:
                return True
            if c not in found:
                found.add(c)
                waiting.append(c)
    return False


def dfs(G, start, goal):
    waiting = [start]
    found = {start}
    while len(waiting) > 0:
        w = waiting.pop() # examine last found
        for c in G[w]:
            if c == goal:
                return True
            if c not in found:
                found.add(c)
                waiting.append(c)
    return False

def bfs_no_graph(start, goal):
    waiting = [start]
    found = {start}
    while len(waiting) > 0:
        w = waiting.pop(0) # examine first found
        # ---
        N=[]
        for i in range(len(w)):
            for a in alpha:
                n = w[:i] + a + w[i+1:]
                if n in words and n != w:
                    N.append(n)
        # ---     
        for c in G[w]:
            if c == goal:
                return True
            if c not in found:
                found.add(c)
                waiting.append(c)
    return False

def dfs_no_graph(start, goal):
    waiting = [start]
    found = {start}
    while len(waiting) > 0:
        w = waiting.pop() # examine last found
        # ---
        N=[]
        for i in range(len(w)):
            for a in alpha:
                n = w[:i] + a + w[i+1:]
                if n in words and n != w:
                    N.append(n)
        # ---     
        for c in G[w]:
            if c == goal:
                return True
            if c not in found:
                found.add(c)
                waiting.append(c)
    return False

def bfs_no_graph_path(start, goal):
    waiting = [start]
    parent = {start:None}
    while len(waiting) > 0:
        w = waiting.pop(0) # examine first found
        # ---
        N=[]
        for i in range(len(w)):
            for a in alpha:
                n = w[:i] + a + w[i+1:]
                if n in words and n != w:
                    N.append(n)
        # --- 
        for x in N:
            if x == goal:
                path = [x]
                x = w
                while parent[x] != None:
                    path.append(x)
                    x = parent[x]
                path.append(x)
                path.reverse()
                return path
            if x not in parent:
                parent[x] = w
                waiting.append(x)
    return []

def dfs_no_graph_path(start, goal):
    waiting = [start]
    parent = {start:None}
    while len(waiting) > 0:
        w = waiting.pop() # examine last found
        # ---
        N=[]
        for i in range(len(w)):
            for a in alpha:
                n = w[:i] + a + w[i+1:]
                if n in words and n != w:
                    N.append(n)
        # ---
        for x in N:
            if x == goal:
                path = [x]
                x = w
                while parent[x] != None:
                    path.append(x)
                    x = parent[x]
                path.append(x)
                path.reverse()
                return path
            if x not in parent:
                parent[x] = w
                waiting.append(x)
    return []

def bfs_path(G, start, goal):
    waiting = [start]
    parent = {start:None}
    while len(waiting) > 0:
        w = waiting.pop(0) # examine first found
        for c in G[w]:
            if c == goal:
                path = [c]
                c = w
                while parent[c] != None:
                    c = parent[c]
                    path.append(c)
                path.reverse()
                return path
            if c not in parent:
                parent[c] = w
                waiting.append(c)
    return []

def dfs_path(G, start, goal):
    waiting = [start]
    parent = {start:None}
    while len(waiting) > 0:
        w = waiting.pop() # examine last found
        for c in G[w]:
            if c == goal:
                path = [c]
                c = w
                while parent[c] != None:
                    c = parent[c]
                    path.append(c)
                path.reverse()
                return path
            if c not in parent:
                parent[c] = w
                waiting.append(c)
    return []

alpha = 'abcdefghijklmnopqrstuvwxyz'

G = Graph()
for w in words:
    G.add(w)

for w in words:
    for i in range(len(w)):
        for a in alpha:
            n = w[:i] + a + w[i+1:]
            if n in words and n != w:
                G.add_edge(w,n)

print(bfs_no_graph_path('wait','lift'))
print(dfs_no_graph_path('wait','lift'))

