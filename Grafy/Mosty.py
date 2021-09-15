# An edge in an undirected connected graph is a BRIDGE if removing it disconnects the graph

time = 0

# for the adjacency list:
# dla listy sasiedztwa:

def DFSVisit(G, u, visited, parent, czasy, low):
    global time
    time += 1
    visited[u] = True
    czasy[u] = time
    low[u] = czasy[u]
    for v in G[u]:
        if not visited[v]:
            parent[v] = u
            DFSVisit(G,v, visited, parent, czasy, low)
        elif parent[u] != v and visited[v]:  #krawedz wsteczna z u do v
            if low[u] > czasy[v]:
                low[u] = czasy[v]
    if parent[u] != None and low[parent[u]] > low[u]:  #u jest dzieckiem parent[u], u ma ostateczna wartosc low
        low[parent[u]] = low[u]


def DFS(G):
    n = len(G)
    visited = [False] * n
    parent = [None] * n
    czasy = [None] * n
    low = [10000] * n
    global time
    time = 0

    for v in range(n):
        if not visited[v]:
            DFSVisit(G, v, visited, parent, czasy, low)
    return parent, czasy, low


def bridges(G):
    n = len(G)
    p, t, l = DFS(G)
    # print(p, t, l)
    res = []
    for v in range(n):
        if t[v] == l[v] and p[v] != None:
            res.append([v, p[v]])
    if res != []:
        return res

G = [[1,3],
     [0,2],
     [1,3,4],
     [0,2],
     [2,5,6],
     [4,6],
     [5,4]]
print(bridges(G))

g = [[1,7],
     [0,2],
     [1,3,6],
     [2,4,5],
     [3,5],
     [4,3],
     [0,2, 7],
     [6]]
print(bridges(g))
