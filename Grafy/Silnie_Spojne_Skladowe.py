# A strongly connected component (SCC) of a directed graph is a maximal strongly connected subgraph.
# pl. silnie spójne skladowe

time = 0

# for the adjacency matrix:
# pl. dla macierzy sasiedztwa:

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


"""G = [[4, 2],
     [0,10],
     [1],
     [4,6],
     [5],
     [3],
     [5],
     [10],
     [7],
     [8,6],
     [9]]
reverse(G)"""
G = [[0 for j in range(11)] for i in range(11)]
G[0][4] = 1
G[0][2] = 1
G[1][0] = 1
G[1][10] = 1
G[2][1] = 1
G[3][4], G[3][6] = 1, 1
G[4][5] = 1
G[5][3] = 1
G[6][5] = 1
G[7][10] = 1
G[8][7] = 1
G[9][8], G[9][6] = 1, 1
G[10][9] = 1
SCC(G)