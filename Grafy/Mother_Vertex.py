time = 0
def DFSVisit_matrix(G, u, visited, times):
    n = len(G)
    global time
    global licz
    visited[u] = True
    for v in range(n):
        if G[u][v] == 1 and not visited[v]:
            visited = DFSVisit_matrix(G,v,visited, times)
    time += 1
    times[u] = time
    return visited


def DFS_matrix(G):
    n = len(G)
    visited = [False] * n
    times = [None] * n
    global time
    time = 0

    for v in range(n):
        if not visited[v]:
            DFSVisit_matrix(G, v,visited,times)
    return times


def Mother_Vertex(G):
    n = len(G)
    times = DFS_matrix(G)
    maks = 0
    for i in range(len(times)):
        if times[i] > maks:
            maks = times[i]
            ind = i
    visited = [False] * n
    visited = DFSVisit_matrix(G, ind, visited, times)
    for i in range(n):
        if not visited[i]:
            return False
    return (True, ind)


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
print(Mother_Vertex(G))