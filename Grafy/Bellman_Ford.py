def Bellman_Ford(G,s):
    n = len(G)
    cost = [10000]*n
    parent = [None]*n
    cost[s] = 0
    edges = []
    for i in range(n):
        for u in G[i]:
            edges.append([i, u[0], u[1]])
    m = len(edges)
    print(m)
    for i in range(n-1):
        for j in range(m):
            if cost[edges[j][1]] > cost[edges[j][0]] + edges[j][2]:
                cost[edges[j][1]] = cost[edges[j][0]] + edges[j][2]
                parent[edges[j][1]] = edges[j][0]
    for i in range(m):
        if cost[edges[i][1]] > cost[edges[i][0]] + edges[i][2]:
            return "CYKL"
    return cost, parent


G = [[(1,0), (2,1)],
    [(3,1), (2,0)],
    [(3,0)],
    []]
print(Bellman_Ford(G,0))
print()
G2 = [
    [(1,3), (2,6), (4,3)],
    [(0,3), (2,1), (3,3)],
    [(0,6), (1,1), (3,3), (5,1)],
    [(1,3), (2,3), (5,1)],
    [(0,3), (5,3)],
    [(4,3), (2,1), (3,1)]
]
print(Bellman_Ford(G2, 0))
