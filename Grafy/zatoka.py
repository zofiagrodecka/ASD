def DFSVisit(G, n, m, u, v, T, visited):
    if u == n-1 and v == m-1:
        return True
    visited[u][v] = True
    if u < n-1 and not visited[u+1][v] and G[u+1][v] > T:
        return DFSVisit(G,n,m,u+1,v,T,visited)
    if v < m-1 and not visited[u][v+1] and G[u][v+1] > T:
        return DFSVisit(G, n, m, u, v + 1, T, visited)
    return False

def DFS(G,T):
    n = len(G)
    m = len(G[0])
    visited = [False] * n  # tablica odwiedzonych
    for i in range(n):
        visited[i] = [False]*m

    if DFSVisit(G, n, m, 0, 0, T, visited):
        return True
    return False


A = [
    [ 3, 4, 5, 6, 7, 0, 3, 1],
    [ 4, 2, 1, -1, 5, 2, 6, 0],
    [ 100, -5, 5, 1, 4, 6, 5, -2],
    [ 9, 90, 0, 5, 2, 2, 77, -7],
    [ 9, 8, 7, 1, 2, 0, 9, 2],
    [ 0, 1, 5, 6,7, 0, 2, 10],
    [ 10, 11, 1, 2, 12, 13, 14, 15]
]
print(DFS(A,2))