def Floyd_Warshall(G):
    n = len(G)
    parent = [[-1 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if G[i][j] == 0:
                G[i][j] = 10000
        G[i][i] = 0
    for i in range(n):
        for j in range(n):
            if G[i][j] < 10000 and G[i][j] != 0:
                parent[i][j] = i
    for t in range(n):
        for i in range(n):
            for j in range(n):
                # G[i][j] = min(G[i][j], G[i][t] + G[t][j])
                if G[i][j] > G[i][t] + G[t][j]:
                    G[i][j] = G[i][t] + G[t][j]
                    parent[i][j] = parent[t][j]
    for i in range(n):
        for j in range(n):
            print(G[i][j], end=' ')
        print()
    print()
    """for i in range(n):
        for j in range(n):
            print(parent[i][j], end=' ')
        print()"""
    return G, parent


def path_recursive(parent, s, t):
    if parent[s][t] >= 0 and parent[s][t] != s:
        path_recursive(parent, s, parent[s][t])
    else:
        print(s)
    print(t)

def print_path(G, s, t):
    G, P = Floyd_Warshall(G)
    path_recursive(P, s, t)


G3 = [[ 0 for i in range(5)] for j in range(5)]
G3[0][1] = 2
G3[1][3] = 3
G3[3][4] = 2
G3[0][2] = 4
G3[1][2] = 3
G3[2][3] = -1
G3[2][4] = 4

g = [
[0, 4 ,0, 0 ],
[0, 0, 0, 0],
[5, 0, 0, 0],
[0, 0, 0, 0]
]

G1 = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 5],
    [0, 2, 0, 0]
]
G2 = [
    [0, 5, 0, 2],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [2, 2, 0, 0]
]
G = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [5, 0, 0, 0],
    [0, 0, 0, 0]
]

Floyd_Warshall(G1)
Floyd_Warshall(G2)
Floyd_Warshall(G)
R1 = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [5, 0, 0, 5],
    [0, 2, 0, 0]
]
R2 = [
    [0, 4, 0, 2],
    [0, 0, 0, 0],
    [5, 0, 0, 0],
    [2, 2, 0, 0]
]
Floyd_Warshall(R1)
Floyd_Warshall(R2)
# print_path(g, 2, 1)