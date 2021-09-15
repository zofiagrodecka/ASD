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
    maks = i
    size = k[0]
    if l <= size and k[l][1] > k[maks][1]:
        maks = l
    if r <= size and k[r][1] > k[maks][1]:
        maks = r
    if maks != i:
        k[i], k[maks] = k[maks], k[i]
        heapify(k, maks)

def getmax(k):
    size = k[0]
    res = k[1]
    k[1] = k[size]
    k[0] -= 1
    heapify(k, 1)
    return res

def insert(k, x):
    k[0] += 1
    size = k[0]
    k[size] = x
    i = size
    while i > 1 and k[i][1] > k[parent(i)][1]:
        k[i], k[parent(i)] = k[parent(i)], k[i]
        i = parent(i)


def dijkstra(G, s):
    n = len(G)
    n_of_people = [0]*n
    visited = [False]*n
    parent = [-1]*n
    Queue = [0]*50
    insert(Queue, (s,10000))
    n_of_people[s] = 10000
    while not empty(Queue):
        u, people = getmax(Queue)
        if not visited[u]:
            visited[u] = True
            for v in range(n):
                if G[u][v] > 0 and min(people, G[u][v]) > n_of_people[v]:
                    n_of_people[v] = min(people, G[u][v])
                    parent[v] = u
                    insert(Queue, (v, n_of_people[v]))
    return n_of_people, parent


G = [[0 for i in range(7)] for j in range(7)]
G[0][1]= 5
G[1][0] = 5
G[1][2] = 3
G[2][1] = 3
G[0][6] = 4
G[6][0] = 4
G[6][2] = 1
G[2][6] = 1
G[2][5] = 3
G[5][2] = 3
G[1][5] = 2
G[5][1] = 2
G[5][4] = 2
G[4][5] = 2
G[5][3] = 1
G[3][5] = 1
G[3][4] = 2
G[4][3] = 2
print(dijkstra(G,0))
