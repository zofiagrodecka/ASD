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
    return dist


def dijkstra_n(G):
    global inf
    n = len(G)
    dist = [[] for i in range(n)]
    for i in range(n):
        dist[i].extend(dijkstra(G, i))
    for i in range(n):
        for j in range(n):
            print(dist[i][j], end=' ')
        print()
    print()


g = [
[0, 4 ,0, 0 ],
[0, 0, 0, 0],
[5, 0, 0, 0],
[0, 0, 0, 0]
]
dijkstra_n(g)