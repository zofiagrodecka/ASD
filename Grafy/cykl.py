#dla listy sasiedztwa:
graf = [[1, 2], [], [3], [4], [2]]
visited = ["bialy"] * len(graf)  # tablica odwiedzonych
parent = [None] * len(graf)  # tablica rodzicow
czasy = [None] * len(graf)
time = 0
stos = []
wynik = []

def DFSVisit(G, u):
    global time
    time += 1
    visited[u] = "szary"
    stos.append(u)
    czasy[u][0] = time
    for v in G[u]: #for po wszystkich sasiadach (v) wierzcholka u
        if visited[v] == "bialy": #or visited[v] == "czarny":
            parent[v] = u
            DFSVisit(G,v)
        else:
            if visited[v] == "szary":
                #if parent[v] != None:
                parent[v] = "cycle"
                return
    visited[u] = "czarny"
    wynik.append(stos.pop())
    time += 1
    czasy[u][1] = time

def DFS(G):
    n = len(G)
    for i in range(n):
        czasy[i] = [0]*2

    for v in range(n):
        if visited[v] == "bialy": #or visited[v] == "czarny":
            DFSVisit(G, v)
    return (visited, parent, czasy, stos, wynik)


print(DFS(graf))