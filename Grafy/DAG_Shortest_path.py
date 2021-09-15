class Node:
    def __init__(self):
        self.next = None
        self.val = None


class Stack:
    def __init__(self):
        self.top = Node()

    def push(self,x):
        node = Node()
        node.val = x
        node.next = self.top.next
        self.top.next = node

    def pop(self):
        res = self.top.next
        self.top.next = res.next
        return res.val

    def is_empty(self):
        return self.top.next == None

    def wypisz(self):
        p = self.top.next
        while p is not None:
            print(p.val, end=' ')
            p = p.next


# for the adjacency list:
# pl. dla listy sasiedztwa:
def DFSVisit(G, u, visited, parent, S):
    n = len(G)
    visited[u] = True
    for v in range(n):
        if G[u][v] > 0 and not visited[v]:
            parent[v] = u
            DFSVisit(G,v, visited, parent, S)
    S.push(u)


def sort_top(G):
    n = len(G)
    visited = [False] * n
    parent = [None] * n
    S = Stack()

    for v in range(n):
        if not visited[v]:
            DFSVisit(G, v, visited, parent, S)
    return S


def shortest(G, s):
    n = len(G)
    distances = [1000]*n
    distances[s] = 0
    stos = sort_top(G)
    while not stos.is_empty():
        u = stos.pop()
        for v in range(n):
            if G[u][v] != 0 and distances[v] > distances[u] + G[u][v]:
                distances[v] = distances[u] + G[u][v]
    return distances


G = [[0 for j in range(6)] for i in range(6)]
G[0][1] = 3
G[0][3] = -1
G[1][5] = 4
G[1][2] = 7
G[2][5] = 5
G[2][4] = 1
G[3][2] = 6
G[3][1] = 2
G[5][4] = -2
print(shortest(G,3))