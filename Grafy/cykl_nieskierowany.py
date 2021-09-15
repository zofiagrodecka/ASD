def DFSVisit(G, visited, parent, u):
    visited[u] = True
    for v in G[u]:
        if not visited[v]:
            parent[v] = u
            DFSVisit(G, visited, parent,v)
        else:
            if v != parent[u]:
                return True, parent, visited
    return False, parent, visited


def detect_cycle(G):
    n = len(G)
    visited = [False] * len(G)
    parent = [None] * len(G)  # tablica rodzicow
    for v in range(n):
        if not visited[v]:
           return DFSVisit(G, visited, parent, v)


g = [[1], [0,2], [1,5,3], [2,4], [3], [2]]
print(detect_cycle(g))