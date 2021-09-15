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


# for the adjacency list:
# (pl.) dla listy sasiedztwa:

def BFS_lista(G, s):
    n = len(G)
    distance = [None]*n  # list of distances
    visited = [False]*n  # list of visited
    parent = [None]*n  # list of parents

    Q = Queue()
    distance[s] = 0
    visited[s] = True
    parent[s] = None
    Q.put(s)
    while not Q.is_empty():
        u = Q.get()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                distance[v] = distance[u] + 1
                parent[v] = u
                Q.put(v)
        # print("queue:", end=' ')
        # Q.wypisz()
    return distance, visited, parent


# for the adjacency matrix:
# (pl.) dla macierzy sasiedztwa:

def BFS_macierz(G,s):
    n = len(G)
    distance = [None] * n  # list of distances
    visited = [False] * n  # list of visited
    parent = [None] * n  # list of parents
    sp_tree = [[] for _ in range(n)]
    Q = Queue()
    distance[s] = 0
    visited[s] = True
    parent[s] = None
    Q.put(s)
    while not Q.is_empty():
        u = Q.get()
        for v in range(n):
            if G[u][v] == 1 and not visited[v]:
                visited[v] = True
                distance[v] = distance[u] + 1
                parent[v] = u
                sp_tree[u].append(v)
                sp_tree[v].append(v)
                Q.put(v)
            else:
                if distance[v] == distance[u] + 1:
                    sp_tree[v].append(u)
                    sp_tree[u].append(v)
        # print("queue: ", end=' ')
        # Q.wypisz()
    return distance, visited, parent

# Finding shortest path from one vertex to another:

def path_recursive(G, parent, s, t):
    if parent[t] >= 0 and parent[t] != s:
        path_recursive(G, parent, s, parent[t] )
    else:
        print(s)
    print(t)


def print_path(G, s, t):
    n = len(G)
    d, v, p = BFS_macierz(G,s)
    for i in range(n):
        if p[i] == None:
            p[i] = -1
    path_recursive(G, p, s, t)

# Finding shortest paths tree:

def shortest(res, visited, parent, i):
    visited[i] = True
    if parent[i] >= 0:
        res[i].append(parent[i])
        res[parent[i]].append(i)
        shortest(res, visited, parent, parent[i])
    return res


def shortest_paths_tree(G):
    n = len(G)
    d, v, p = BFS_lista(G,0)
    visited = [False]*n
    res = [[] for x in range(n)]
    for i in range(n):
        if p[i] == None:
            p[i] = -1
    for i in range(n-1, -1, -1):
        if not visited[i]:
            res = shortest(res, visited, p, i)
    return res


graf = [[1, 2], [2], []]
graf2 = [
    [0, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0]
]
print(BFS_lista(graf,0))
print(shortest_paths_tree(graf))
print_path(graf2, 0, 6)