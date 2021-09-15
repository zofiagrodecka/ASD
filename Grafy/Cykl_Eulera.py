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
        print("deleted ", res.val, " element")
        return res.val

    def is_empty(self):
        return self.top.next == None

    def wypisz(self):
        p = self.top.next
        while p is not None:
            print(p.val, end=' ')
            p = p.next


# for the adjacency matrix:
# (pl.) dla macierzy sasiedztwa:
def DFSVisit_matrix(G, u, S):
    n = len(G)
    for v in range(n):
        if G[u][v] == 1:
            G[u][v] = 0
            G[v][u] = 0
            DFSVisit_matrix(G,v, S)
    S.push(u)


def euler_cycle(G):
    n = len(G)
    odd = -1  # vertex with an odd degree  (pl. wierzcholek o stopniu nieparzystym)
    n_even = 0  # number of vertexes with even degrees  (pl. ilosc wierzcholkow o stopniu parzystym)
    degrees = [0] * n

    for u in range(n):  # counting degrees of every vertex:
        for v in range(n):
            if G[u][v] == 1:
                degrees[u] += 1
    for i in range(n):
        if degrees[i] % 2 == 0:
            n_even += 1
        else:
            odd = i
    if n_even == n or n_even == n-2:
        S = Stack()
        if odd != -1:  # half-eulerian graph
            DFSVisit_matrix(G, odd, S)
        else:
            DFSVisit_matrix(G, 0, S)
        S.wypisz()
        return True
    else:
        return False


# for the adjacency list
# (pl.) dla listy sasiedztwa
def DFSVisit(G, u, S):
    for v in G[u]:
        G[u].remove(v)  # usuwam krawedz u-v
        G[v].remove(u)  # usuwam krawedz v-u
        DFSVisit(G,v, S)
    S.push(u)


def Euler_cycle(G):
    n = len(G)
    odd = -1  # vertex with an odd degree  (pl. wierzcholek o stopniu nieparzystym)
    n_even = 0  # number of vertexes with even degrees  (pl. ilosc wierzcholkow o stopniu parzystym)
    degrees = [0] * n

    for u in range(n):  # counting degrees of every vertex:
        degrees[u] = len(G[u])
    for i in range(n):
        if degrees[i] % 2 == 0:
            n_even += 1
        else:
            odd = i
    if n_even == n or n_even == n - 2:
        S = Stack()
        if odd != -1:  # half-eulerian graph
            DFSVisit(G, odd, S)
        else:
            DFSVisit(G, 0, S)
        S.wypisz()
        return True
    else:
        return False


Graf = [[0, 1, 0, 0, 1, 0, 0],
     [1, 0, 1, 0, 1, 0, 1],
     [0, 1, 0, 1, 0, 1, 1],
     [0, 0, 1, 0, 0, 1, 0],
     [1, 1, 0, 0, 0, 1, 1],
     [0, 0, 1, 1, 1, 0, 1],
     [0, 1, 1, 0, 1, 1, 0]]
print(euler_cycle(Graf))

g = [[0 for j in range(6)] for i in range(6)]
g[0][1] = 1
g[1][0], g[1][2], g[1][4] = 1, 1, 1
g[2][1], g[2][3] = 1, 1
g[3][2], g[3][4] = 1, 1
g[4][1], g[4][3], g[4][5] = 1, 1, 1
g[5][4] = 1
print(euler_cycle(g))

G = [[0 for j in range(5)] for i in range(5)]
G[0][1] = 1
G[1][0], G[1][2], G[1][4] = 1, 1, 1
G[2][1], G[2][3] = 1, 1
G[3][2], G[3][4] = 1, 1
G[4][1], G[4][3]= 1, 1
print(euler_cycle(G))

G2 = [
    [1,4],
    [0,4,2,6],
    [1,3,5,6],
    [2,5],
    [6,5,0,1],
    [4,6,2,3],
    [1,2,4,5]
]
print(Euler_cycle(G2))