#dla listy sasiedztwa:
def DFSVisit(G, skladowa, visited, parent, u):
    visited[u] = True
    for v in G[u]:
        if not visited[v]:
            parent[v] = u
            skladowa[v] = skladowa[u]
            DFSVisit(G, skladowa, visited, parent, v)

def DFS(G):
    n = len(G)
    visited = [False] * len(G)  # tablica odwiedzonych
    parent = [None] * len(G)  # tablica rodzicow
    skladowa = [None] * len(G)  # tablica skladowych
    licz = 0

    for v in range(n):
        if not visited[v]:
            skladowa[v] = v
            DFSVisit(G, skladowa, visited, parent, v)
            licz += 1
    return (licz, skladowa)


graf = [[1,2],[2],[4],[1],[5],[3],[7],[]]
print(DFS(graf))
g=[[1,3,4],[0,2],[1,3,4],[0,2,5],[0,2],[3]]
print(DFS(g))