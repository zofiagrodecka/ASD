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
        return res.val

    def wypisz(self):
        p = self.head.next
        while p is not None:
            print(p.val, end=' ')
            p = p.next

def BFS(G, s, t, zad, k):
    n = len(G)
    visited = [False]*n  # tablica odwiedzonych
    distance = [-1] * n  # list of distances
    length = [0]*n

    Q = Queue()
    visited[s] = True
    Q.put(s)
    if zad == 1:
        while not Q.is_empty():
            u = Q.get()
            if u == t:
                return True
            for v in range(n):
                if G[u][v] == 1 and not visited[v]:
                    visited[v] = True
                    Q.put(v)
        return False
    if zad == 2:
        distance[s] = 0
        while not Q.is_empty():
            u = Q.get()
            for v in range(n):
                if G[u][v] == 1 and not visited[v]:
                    visited[v] = True
                    distance[v] = distance[u] + 1
                    length[v] = v - s
                    if distance[v] < k:
                        Q.put(v)
        return max(length)


def make_graph(tab):
    n = len(tab)
    maks = 0
    for i in range(n):
        if tab[i][0] > maks:
            maks = tab[i][0]
        if tab[i][1] > maks:
            maks = tab[i][1]
    G = [0]*(maks + 1)
    for i in range(maks + 1):
        G[i] = [0] * (maks + 1)
    for i in range(n):
        G[tab[i][0]][tab[i][1]] = 1
        G[tab[i][1]][tab[i][0]] = 1
    return G, maks


def sklej(tab, a, b):  # czy da sie uzyskac przedzial [a,b] przez sklejanie odcinkow
    G, m = make_graph(tab)
    print(G)
    return BFS(G, a, b, 1, 0)


def max_odc(tab, k):  # jaki najdluzszy odcinek da sie otrzymac sklejajc najwyzej k odcinkow
    n = len(tab)
    G, m = make_graph(tab)
    maks = 0
    for i in range(m + 1):
        dlugosc = BFS(G, i, 0, 2, k)
        if dlugosc > maks:
            maks = dlugosc
    return maks



tab = [(1,5), (5,6), (1,3), (2,8)]
print(sklej(tab, 1,6))
print(max_odc(tab,1))