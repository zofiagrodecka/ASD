class Node:
    def __init__(self):
        self.val = None
        self.next = None


class Queue:
    def __init__(self):
        self.head = Node()  # sentinel node (pl. wartownik)
        self.head.next = None
        self.tail = None

    def is_empty(self):
        return not self.head.next

    def put(self,x):  # enqueue
        node = Node()
        node.val = x
        self.tail = node
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = node

    def get(self):
        res = self.head.next
        self.head.next = res.next
        # print("deleted: ", res.val, " element")
        return res.val

    def wypisz(self):
        p = self.head.next
        while p is not None:
            print(p.val, end=' ')
            p = p.next


def BFS_macierz(G,s):
    n = len(G)
    res = [[] for x in range(n)]
    distance = [None] * n  # list of distances
    visited = [False] * n  # list of visited
    parent = [[] for _ in range(n)]  # list of parents
    Q = Queue()
    distance[s] = 0
    visited[s] = True
    parent[s].append(-1)
    Q.put(s)
    while not Q.is_empty():
        u = Q.get()
        for v in range(n):
            if G[u][v] == 1:
                if not visited[v]:
                    visited[v] = True
                    distance[v] = distance[u] + 1
                    parent[v].append(u)
                    res[v].append(u)
                    res[u].append(v)
                    Q.put(v)
                else:
                    if distance[v] == distance[u] + 1:
                        parent[v].append(u)
                        res[v].append(u)
                        res[u].append(v)
    return ( parent, res )


def BFS_lista(G, s, t):
    n = len(G)
    distance = [None]*n  # list of distances
    visited = [False]*n  # list of visited
    parent = [[] for _ in range(n)]  # list of parents
    res = [[] for _ in range(n)]
    Q = Queue()
    distance[s] = 0
    visited[s] = True
    parent[s] = None
    Q.put(s)
    while not Q.is_empty():
        u = Q.get()
        if u == t:
            return res
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                distance[v] = distance[u] + 1
                res[v].append(u)
                res[u].append(v)
                Q.put(v)
            else:
                if distance[v] == distance[u] + 1:
                    res[v].append(u)
                    res[u].append(v)
    return res

time = 0

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
    for v in range(n):
        if t[v] == l[v] and p[v] != None:
            return True
    return False


def exists(G, s, t):
    n = len(G)
    p, shortest_paths_tree = BFS_macierz(G, s)
    # print(p, shortest_paths_tree)
    res = BFS_lista(shortest_paths_tree, t, s)
    # print(res)
    return bridges(res)


graf = [
    [0, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
]

G = [[0 for i in range(9)] for j in range(9)]
G[0][1] = 1
G[0][2] = 1
G[1][3] = 1
G[3][5] = 1
G[2][4] = 1
G[4][5] = 1
G[5][6] = 1
G[5][7] = 1
G[7][8] = 1
G[6][8] = 1
print(exists(graf, 0, 7))