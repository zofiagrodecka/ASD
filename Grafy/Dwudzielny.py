# for the adjacency list:
# pl. dla listy sasiedztwa:

def DFSVisit(G, u, visited, colours):
    visited[u] = True
    for v in G[u]:
        if not visited[v]:
            colours[v] = (-1)*colours[u]
            if DFSVisit(G,v, visited, colours):
                return True
            else:
                return False
        else:
            if colours[v] == colours[u]:
                return False
    return True


def bipartite(G):
    n = len(G)
    visited = [False] * n
    colours = [0]*n

    for v in range(n):
        if not visited[v]:
            colours[v] = 1
            if not DFSVisit(G, v, visited, colours):
                return False
    return True


G = [[1, 3],
    [0, 2],
    [1, 3],
    [0, 4],
    [3]]
G2 = [[1, 3],
    [0, 2, 3],
    [1, 3],
    [0, 1, 2]]
G3 = [
    [9, 7],
    [7],
    [8],
    [6, 8],
    [5, 7],
    [4],
    [3],
    [0, 4, 1],
    [3, 2],
    [0]
]
print(bipartite(G3))