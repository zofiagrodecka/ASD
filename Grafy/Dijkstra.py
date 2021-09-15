from queue import PriorityQueue

def dijkstra(G, s):
    n = len(G)
    cost = [1000000]*n  # infinity
    parent = [None]*n
    visited = [False]*n  # tablica juz przetworzonych wierzcholkow
    Q = PriorityQueue()
    cost[s] = 0
    tup = (0, s)  # tuple: (cost of the edge, number of the vertex)  (pl. (koszt krawedzi, numer wierzcholka))
    Q.put(tup)
    while not Q.empty():
        k = Q.get()  # krotka z kolejki: (koszt krawedzi, numer wierzcholka)
        w = k[1]  # number of vertex taken out of queue (pl. numer wierzcholka w wyjetego z kolejki)
        if not visited[w]:  # przetwarzam wierzcholek zaraz po wyjeciu go z kolejki, jesli jeszcze nie byl przetworzony
            visited[w] = True
            for v in G[w]:  # v jest krotka (wierzcholek, koszt)
                if cost[v[0]] > cost[w] + v[1]:  # Relax(w,v)
                    cost[v[0]] = cost[w] + v[1]
                    parent[v[0]] = w
                    tmp = [cost[v[0]], v[0]]
                    tup = tuple(tmp)  # tworze krotke z nastepnego wierzcholka do kolejki priorytetowej
                    Q.put(tup)
    return cost


# np. G[i] = [(7,0), (4,1), (8,1), (2,0)] oznacza, że z wierzchołka
# i są krawędzie do wierzchołków 7 (koszt 0), 4 (koszt 1), # 8 (koszt 1) i 2 (koszt 0)
G = [[(1,0), (2,1)],
    [(3,1), (2,0)],
    [(3,0)],
    []]

print( dijkstra( G, 0 ) ) # wypisze [None,0,1,2]
print()

#moj przyklad
G2 = [
    [(1,3), (2,6), (4,3)],
    [(0,3), (2,1), (3,3)],
    [(0,6), (1,1), (3,3), (5,1)],
    [(1,3), (2,3), (5,1)],
    [(0,3), (5,3)],
    [(4,3), (2,1), (3,1)]
]
print( dijkstra( G2, 0 ) )