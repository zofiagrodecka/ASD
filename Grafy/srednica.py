last = None
max_path = 0

def DFSVisit(G, u, visited, parent, path, res):
    global max_path
    global last
    path += 1
    visited[u] = True
    res.append(u)
    for v in G[u]:  # for po wszystkich sasiadach (v) wierzcholka u
        if not visited[v]:
            parent[v] = u
            DFSVisit(G,v, visited, parent, path, res)
    if max_path < path:
        max_path = path
        last = u


def diameter(G):
    n = len(G)
    visited = [False] * n  # tablica odwiedzonych
    parent = [None] * n  # tablica rodzicow
    res = []
    global max_path
    DFSVisit(G, 0, visited, parent, 0, res)
    # print(last, max_path)
    for i in range(n):
        visited[i] = False
        parent[i] = None
    res = []
    # print("once again")
    max_path = 0
    DFSVisit(G, last, visited, parent, 0, res)
    # print(last)
    return res


g=[[1,3,4],[0,2],[1,4],[0, 4,5],[3, 0, 2],[3, 6],[7, 5], [6]]
print(diameter(g))