inf = 10000

def Bellman_Ford(G, s):
    n = len(G)
    global inf
    dist = [inf]*n
    parent = [None] * n
    dist[s] = 0
    for i in range(n - 1):
        for u in range(n):
            for v in range(n):  # dla kazdej krawedzi
                if G[u][v] > 0 and dist[v] > dist[u] + G[u][v]:
                    dist[v] = dist[u] + G[u][v]
                    parent[v] = u
    # Czy cykl ujemny ?
    for u in range(n):
        for v in range(n):
            if G[u][v] > 0 and dist[v] > dist[u] + G[u][v]:
                return "CYKL"
    return dist, parent


G = [[0 for j in range(6)] for i in range(6)]
G[0][1] = 3
G[1][0] = 3
G[1][2] = 2
G[2][1] = 2
G[2][3] = 3
G[3][2] = 3
G[3][4] = 2
G[4][3] = 2
G[4][5] = 1
G[5][4] = 1
G[5][0] = 4
G[0][5] = 4
G[1][5] = 1
G[5][1] = 1
G[5][2] = 2
G[2][5] = 2
print(Bellman_Ford(G, 0))