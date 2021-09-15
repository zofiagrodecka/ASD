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


inf = 100000
def dijkstra(G, s):
    n = len(G)
    global inf
    dist = [inf]*n
    visited = [False]*n
    parent = [None]*n
    Queue = [0]*50

    dist[s] = 0
    insert(Queue, (s, 0))
    while not empty(Queue):
        u, cost = getmin(Queue)
        if not visited[u]:
            visited[u] = True
            for v in range(n):
                if G[u][v] > 0 and dist[v] > dist[u] + G[u][v]:
                    dist[v] = dist[u] + G[u][v]
                    parent[v] = u
                    insert(Queue, (v, dist[v]))
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
print(dijkstra(G, 0))