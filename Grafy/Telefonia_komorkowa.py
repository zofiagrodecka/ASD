class Node:
    def __init__(self):
        self.next = None
        self.val = None


# for the adjacency list:
# pl. dla listy sasiedztwa:

def DFSVisit(G, u, visited, parent):
    visited[u] = True
    for v in G[u]:
        if not visited[v]:
            parent[v] = u
            DFSVisit(G,v, visited, parent)
    print(u)


def PAUSE(G):
    n = len(G)
    visited = [False] * n
    parent = [None] * n

    for v in range(n):
        if not visited[v]:
            DFSVisit(G, v, visited, parent)



G = [[2, 4, 1],
    [2, 3],
    [],
    [6,5],
    [3],
    [],
    []]
PAUSE(G)
print()
