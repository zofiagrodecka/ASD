class Node:
    def __init__(self):
        self.val = None
        self.next = None

class Queue:
    def __init__(self):
        self.head = Node() #wartownik
        self.head.next = None
        self.tail = None

    def is_empty(self):
        return not self.head.next

    def put(self,x): #enqueue
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
        #print("usunalem ", res.val, " element")
        return res.val

    def wypisz(self):
        p = self.head.next
        while p is not None:
            print(p.val, end=' ')
            p = p.next

def BFS(G,s):
    n = len(G)
    distance = [None] * n  # tablica odleglosci
    visited = [False] * n  # tablica odwiedzonych
    parent = [-1] * n  # tablica rodzicow

    Q = Queue()
    distance[s] = 0
    visited[s] = True
    parent[s] = -1
    Q.put(s)
    while not Q.is_empty():
        u = Q.get()
        for v in range(n):
            #print("wierzcholek: ", v)
            if G[u][v] > 0 and not visited[v]:
                #print("wierzch ", v, "nieodwiedzony")
                visited[v] = True
                distance[v] = distance[u] + 1
                parent[v] = u
                Q.put(v)
        #print("kolejka:")
        #Q.wypisz()
    return parent

path = []
end = False

def minimal_path(residual, parent, i ,val):
    global path
    if parent[i] >= 0:
        if val > residual[parent[i]][i]:
            val = residual[parent[i]][i]
        val = minimal_path(residual, parent, parent[i], val)
    path.append((parent[i], i))
    return val

def find_argumenting_path(residual, s, t):
    # wybieram najkrótszą (o najmniejszej ilosci krawedzi) z wszystkich sciezek laczacych s z t => BFS
    global end
    parent = BFS(residual, s)
    #print("parent: ", parent)
    if parent[t] == -1:
        end = True
    return minimal_path(residual, parent, t, 10000)


def max_flow( c, s, t ):
    # policz maksymalny przepływ z s do t
    # c[i][j] to przepustowość krawędzi z i do j
    # jeśli c[i][j] > 0 to c[j][i] = 0
    global end
    n = len(c)
    global path
    f = 0
    residual = c
    F = [[0 for j in range(n)] for i in range(n)] #nasze plywy
    global end
    while not end:
        path = []
        powiekszenie = find_argumenting_path(residual, s, t)
        if end:
            break
        #print("powiekszenie: ", powiekszenie)
        if powiekszenie > 0:
            f += powiekszenie
            #print(path)
            for i in path:
                if i[0] != -1:
                    if c[i[0]][i[1]] > 0: #krawedz z argumenting path istnieje w naszym oryginalnym grafie
                        F[i[0]][i[1]] += powiekszenie
                    elif c[i[0]][i[1]] == 0:
                        F[i[1]][i[0]] = 0
                    residual[i[0]][i[1]] = c[i[0]][i[1]] - F[i[0]][i[1]]
                    residual[i[1]][i[0]] = F[i[0]][i[1]]
                    #print(F, residual)
    return f

# --------------------------------------------------------------------------------------
def DFSVisit(G, u, visited, colours):
    n = len(G)
    visited[u] = True
    for v in G[u]: #for po wszystkich sasiadach (v) wierzcholka u
        if not visited[v]:
            colours[v] = (-1)*colours[u]
            if DFSVisit(G,v, visited, colours):
                return True
    return True

def dwudzielny(G):
    n = len(G)
    visited = [False] * n  # tablica odwiedzonych
    colours = [0]*n

    for v in range(n):
        if not visited[v]:
            colours[v] = 1
            if not DFSVisit(G, v, visited, colours):
                return False
    return colours



def skojarzenie(G):
    n = len(G)
    # dla listy:
    C = [[0 for j in range(n + 2)] for i in range(n + 2)]
    start = n
    finish = n+1
    for u in range(n):
        for v in range(len(G[u])):
            C[u][G[u][v]] = 1
    """"# dla macierzy:
    C = G"""
    # robię graf skierowany:
    colours = dwudzielny(G)
    print(colours)
    for i in range(n):
        if colours[i] == -1:
            C[i][finish] = 1
            for j in range(n):
                if C[i][j] == 1:
                    C[i][j] = 0
        else:
            C[start][i] = 1
    for i in range(n+2):
        for j in range(n+2):
            print(C[i][j], end=' ')
        print()
    return max_flow(C, start, finish)


G = [
    [9, 7],
    [7],
    [8],
    [6, 8],
    [5, 7],
    [4],
    [3],
    [0, 4, 1],
    [3, 2],
    [0]
]
print(skojarzenie(G))