# moja wlasna kolejka priorytetowa typu min na heapie

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
    # print("wstawiam: ", x)
    k[0] += 1
    size = k[0]
    k[size] = x
    i = size
    while i>1 and k[i][1] < k[parent(i)][1]:
        k[i], k[parent(i)] = k[parent(i)], k[i]
        i = parent(i)

def dijkstra(G,s):
    n = len(G)
    visited = [[False for i in range(2)] for j in range(n)]
    cost = [1000]*n
    parent = [-1]*n
    who_finishes = [-1]*n
    Q = [0]*10000
    cost[s] = 0
    insert(Q, (s, 0, 0))  # Bob
    insert(Q, (s, 0, 1))  # Alicja
    while not empty(Q):
        u, dist, is_Alice = getmin(Q)
        if is_Alice:
            ind = 1
        else:
            ind = 0
        if not visited[u][ind]:
            visited[u][ind] = True
            for v in range(n):
                if is_Alice:
                    if G[u][v] > -1 and cost[v] > cost[u] + G[u][v]:
                        cost[v] = cost[u] + G[u][v]
                        parent[v] = u
                        who_finishes[v] = is_Alice
                        insert(Q, (v, cost[v], 0))
                else:
                    if G[u][v] > -1 and cost[v] > cost[u]:
                        cost[v] = cost[u]
                        parent[v] = u
                        who_finishes[v] = 0
                        insert(Q, (v, cost[v], 1))
    return parent, cost, who_finishes


def path(parent, i, is_Alice):
    if parent[i] > -1:
        print(i)
        if is_Alice:
            path(parent, parent[i], not is_Alice)
        else:
            path(parent, parent[i], is_Alice)
    else:
        if is_Alice:
            print("A")
        else:
            print("B")


def Alicja_Bob(G, s, t):
    p, dist, who = dijkstra(G, s)
    path(p, t, who[t])


G = [[-1 for i in range(9)] for j in range(9)]
G[0][5] = 5
G[5][0] = 5
G[0][1] = 4
G[1][0] = 4
G[5][4] = 2
G[4][5] = 2
G[0][3] = 8
G[3][0] = 8
G[4][3] = 1
G[3][4] = 1
G[4][6] = 7
G[6][4] = 7
G[3][2] = 2
G[2][3] = 2
G[1][3] = 3
G[3][1] = 3
G[2][7] = 5
G[7][2] = 5
G[7][6] = 1
G[6][7] = 1
G[6][8] = 8
G[8][6] = 8
G[7][8] = 4
G[8][7] = 4
Alicja_Bob(G, 0, 8)