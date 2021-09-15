def DFSVisit_matrix(G, u, visited, times, i):
    n = len(G)
    global time
    global licz
    visited[u] = True
    for v in range(n):
        if G[u][v] == 1 and not visited[v]:
            DFSVisit_matrix(G,v,visited, times, i)
    time += 1
    times[u] = time
    if i == 2:  # DFS for the second time
        print(u, end=' ')


def DFS_matrix(G):
    n = len(G)
    visited = [False] * n
    times = [None] * n
    global time
    time = 0

    for v in range(n):
        if not visited[v]:
            DFSVisit_matrix(G, v,visited,times, 1)
    return times


def reverse(G):
    n = len(G)
    G2 = [0] * n
    for i in range(n):
        G2[i] = [0]*n
    for u in range(n):
        for v in range(n):
            if G[u][v] == 1:
                G2[v][u] = 1
    return G2


def fun(x):
    return x[1]


def SCC(G):
    n = len(G)
    t = DFS_matrix(G)
    G = reverse(G)
    times = []
    for i in range(n):
        times.append([i, t[i]])
    times.sort(reverse=True, key=fun)

    visited = [False] * n
    for u in times:
        if not visited[u[0]]:
            DFSVisit_matrix(G, u[0], visited, t, 2)
            print()


def car_races(G):
    n = len(G)
    edges = []
    for u in range(n):
        for v in G[u]:
            edges.append((u,v))
    m = len(edges)
    graph = [[[0 for i in range(2)] for j in range(m)] for k in range(m)]
    print(graph)



G = [
    [2, 4],
    [5],
    [6, 3],
    [1, 4],
    [1, 2],
    [6],
    [0, 3]]
car_races(G)