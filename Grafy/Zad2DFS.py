def DFSVisit(G, visited, parent, u):
    visited[u] = True
    for v in G[u]: #dla kazdego wierzcholka v sasiadujacego z wierzcholkiem u
        if not visited[v]:
            parent[v] = u
            DFSVisit(G, visited, parent, v)

def DFS(G):
    n = len(G)
    visited = [False] * len(G)  # tablica odwiedzonych
    parent = [None] * len(G)  # tablica rodzicow

    for v in range(n): #dla kazdego wierzcholka w grafie
        if not visited[v]:
            DFSVisit(G, visited, parent, v)
    return (parent)


# elementarny test. Może wypisać np.
# [None, 0, 1, 2]
G = [[1,2],[0,2,3],[3,1,0],[1,2]]
print( DFS(G) )
#moj test
g=[[1,3,4],[0,2],[1,3,4],[0,2,5],[0,2],[3]]
print(DFS(g))