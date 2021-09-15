def DFSVisit_matrix(G, u, y, visited, prev_edge):
    n = len(G)
    m = len(visited)
    if u == y:
        return True
    for v in range(n):
        if G[u][v] > 0 and G[u][v] < prev_edge and not visited[G[u][v]]:
            if DFSVisit_matrix(G,v, y, visited, G[u][v]):
                return True
    return False


def DFS_matrix(G, n_of_edges, x, y):
    n = len(G)
    visited_edges = [False]*(n_of_edges+1)  # list of visited edges
    return DFSVisit_matrix(G, x, y, visited_edges,  n_of_edges + 1)


G = [[0 for j in range(6)] for i in range(6)]
G[0][1] = 1
G[1][0] = 1
G[1][3] = 3
G[3][1] = 3
G[1][5] = 2
G[5][1] = 2
G[0][2] = 6
G[2][0] = 6
G[2][3] = 8
G[3][2] = 8
G[3][4] = 7
G[4][3] = 7
G[2][4] = 5
G[4][2] = 5
G[5][4] = 4
G[4][5] = 4
if DFS_matrix(G, 8, 1, 4):
    print("TAK")
else:
    print("NIE")