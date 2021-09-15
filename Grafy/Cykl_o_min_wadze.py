def Floyd_Warshall(G):
    n = len(G)
    for t in range(n):
        for i in range(n):
            for j in range(n):
                G[i][j] = min(G[i][j], G[i][t] + G[t][j])
    for i in range(n):
        for j in range(n):
            print(G[i][j], end=' ')
        print()
    return G


def min_weighted_cycle(G):
    n = len(G)
    for i in range(n):
        for j in range(n):
            if G[i][j] == 0:
                G[i][j] = 100000
    res = Floyd_Warshall(G)
    mini = 10000
    for i in range(n):
        for j in range(n):
            if G[i][j] + G[j][i] < mini:
                mini = G[i][j] + G[j][i]
                u = i
                v = j
    return mini


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
print(min_weighted_cycle(G))