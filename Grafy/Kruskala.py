class Node:
    def __init__(self, id):
        self.id = id
        self.parent = self
        self.rank = 0


def find_set(x):
    if x != x.parent:
        x.parent = find_set(x.parent)
    return x.parent


def union(x,y):
    x = find_set(x)
    y = find_set(y)
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


def fun(x):
    return x[2]


def Kruskal(G):
    n = len(G)
    MST = []
    edges = []
    forest = [None]*n
    for u in range(n):
        for v in range(n):
            if G[u][v] > 0:
                G[v][u] = 0
                edges.append([u, v, G[u][v]])  # (vetex u, vertex v, weight of edge)
    edges.sort(key=fun)
    for i in range(n):
        forest[i] = Node(i)
    for e in edges:
        if find_set(forest[e[0]]) != find_set(forest[e[1]]):
            new = (e[0], e[1])
            MST.append(new)
            union(forest[e[0]], forest[e[1]])
    return MST


G = [[0 for j in range(7)] for i in range(7)]
G[0][1] = 3
G[1][0] = 3
G[1][3] = 3
G[3][1] = 3
G[3][5] = 1
G[5][3] = 1
G[5][4] = 3
G[4][5] = 3
G[0][4] = 3
G[4][0] = 3
G[0][2] = 6
G[2][0] = 6
G[1][2] = 1
G[2][1] = 1
G[2][3] = 3
G[3][2] = 3
G[2][5] = 1
G[5][2] = 1
print(Kruskal(G))