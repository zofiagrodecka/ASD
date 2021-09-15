time = 0

# for the adjacency list:
# (pl.) dla listy sasiedztwa:

def DFSVisit(G, u, visited, parent, times):
    global time
    time += 1
    visited[u] = True
    times[u][0] = time
    for v in G[u]:
        if not visited[v]:
            parent[v] = u
            DFSVisit(G,v, visited, parent, times)
    time += 1
    times[u][1] = time


def DFS(G):
    n = len(G)
    visited = [False] * n  # list of visited
    parent = [None] * n  # list of parents
    times = [None] * n
    global time
    time = 0
    for i in range(n):
        times[i] = [0]*2

    for v in range(n):
        if not visited[v]:
            DFSVisit(G, v, visited, parent, times)
    return (visited, parent, times)


# for the adjacency matrix:
# (pl.) dla macierzy sasiedztwa:

def DFSVisit_matrix(G, u, visited, parent, times):
    n = len(G)
    global time
    time += 1
    visited[u] = True
    times[u][0] = time
    for v in range(n):
        if G[u][v] == 1 and not visited[v]:
            parent[v] = u
            DFSVisit_matrix(G,v,visited, parent, times)
    time += 1
    times[u][1] = time


def DFS_matrix(G):
    n = len(G)
    visited = [False] * n  # list of visited
    parent = [None] * n  # list of parents
    times = [None] * n
    global time
    time = 0
    for i in range(n):
        times[i] = [0]*2

    for v in range(n):
        if not visited[v]:
            DFSVisit_matrix(G, v,visited,parent,times)
    return (visited, parent, times)


# finding DFS forest:

def forest_recursive(res, visited, parent, i):
    visited[i] = True
    if parent[i] >= 0:
        res[i].append(parent[i])
        res[parent[i]].append(i)
        forest_recursive(res, visited, parent, parent[i])
    return res


def DFS_forest(G):
    n = len(G)
    v, p, t = DFS(G)
    visited = [False]*n
    res = [[] for x in range(n)]
    for i in range(n):
        if p[i] == None:
            p[i] = -1
    for i in range(n-1, -1, -1):
        if not visited[i]:
            res = forest_recursive(res, visited, p, i)
    return res


graf = [[1], [2], [0]]
macierz = [[0, 1, 1, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 1, 1, 0], [0, 0, 0, 1, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0,0,0,0,0,0,0,0]]
print(DFS(graf))
# elementarny test. Może wypisać np.
# [None, 0, 1, 2]
G = [[1,2],[0,2,3],[3,1,0],[1,2]]
print( DFS(G) )
# moj test
g=[[1,3,4],[0,2],[1,4],[0,5],[0,2],[3]]
print(DFS(g))
print(DFS_forest(g))