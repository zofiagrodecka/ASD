
# priority queue
def parent(i):
    return i//2

def left(i):
    return i*2

def right(i):
    return 2*i + 1

def empty(k):
    if k[0] == 0:
        return True
    else:
        return False


def heapify(k, i):
    l = left(i)
    r = right(i)
    mini = i
    size = k[0]
    if l <= size and k[l][1] < k[mini][1]:
        mini = l
    if r <= size and k[r][1] < k[mini][1]:
        mini = r
    if mini != i:
        k[i], k[mini] = k[mini], k[i]
        heapify(k, mini)


def getmin(k):
    res = k[1]
    size = k[0]
    k[1] = k[size]
    k[0] -= 1
    heapify(k,1)
    return res


def insert(k, x):
    k[0] += 1
    size = k[0]
    k[size] = x
    i = size
    while i>1 and k[i][1] < k[parent(i)][1]:
        k[i], k[parent(i)] = k[parent(i)], k[i]
        i = parent(i)


def Prim(G, s):
    n = len(G)
    q = [0]*(n*10)  # priority queue
    waga = [1000]*n  # waga kazdego wierzcholka
    parent = [None]*n
    processed = [False]*n
    waga[s] = 0
    insert(q, (s,0))  # (number of vertex, weight of an edge)
    while not empty(q):
        u = getmin(q)
        for v in G[u[0]]:
            if waga[v[0]] > v[1]:
                waga[v[0]] = v[1]
                if not processed[v[0]]:
                    parent[v[0]] = u[0]
                insert(q, v)
        processed[u[0]] = True
    return waga, parent


# (wierzcholek, waga)
# np wierzcholek 0 łaczy sie z wierzcholkiem 1 krawedzią o wadze 4
# wierzcholek 0 łaczy sie z 4 krawedzia o wadze 1
# itd
G = [[(1,4), (4,1), (5,2)],
     [(0,4), (4,2), (2,2)],
     [(1,2), (3,8)],
     [(5,6), (4,3), (2,8), ],
     [(0,1), (1,2), (3,3), (5,7)],
     [(0,2), (3,6)]]
G2 = [
    [(1,3), (4,3), (2,6)],
    [(0,3), (2,1), (3,3)],
    [(0,6), (1,1), (3,3), (5,1)],
    [(1,3), (2,3), (5,1)],
    [(5,3), (0,3)],
    [(4,3), (2,1), (3,1)]
]
print(Prim(G,0))