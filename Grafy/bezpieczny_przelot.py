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


def BFS(G, x, y, t):
    n = len(G)
    Q = Queue()
    visited = [None]*n
    mini = 10000
    maksi = 0
    for v in range(n):
        if G[x][v] > 0:
            if v == y:
                return (True, G[x][y])
            if G[x][v] - t > 0:
                begin = G[x][v] - t
            else:
                begin = 1
            if begin < mini:
                mini = begin
            if G[x][v]+t+1 > maksi:
                maksi = G[x][v]+t+1
            for i in range(begin, G[x][v]+t+1):
                if v != x:
                    Q.put((v, i))
    m = maksi - mini + 1
    for i in range(n):
        visited[i] = [False]*m
    while not Q.is_empty():
        u, pulap = Q.get()
        for v in range(n):
            if G[u][v] > 0 and not visited[v][pulap-mini] and abs(G[u][v] - pulap) <= t:
                visited[v][pulap-mini] = True
                if v == y:
                    return (True, pulap)
                Q.put((v, pulap))
        # print("queue: ", end=' ')
        # Q.wypisz()
    return False


G = [[0 for j in range(6)] for i in range(6)]
G[0][1] = 3
G[1][0] = 3
G[1][2] = 8
G[2][1] = 8
G[3][4] = 6
G[4][3] = 6
G[4][5] = 1
G[5][4] = 1
G[5][0] = 5
G[0][5] = 5
G[0][4] = 2
G[0][3] = 7
G[1][5] = 5
G[1][3] = 2
G[2][4] = 3
G[3][2] = 1
G[3][0] = 7
G[4][2] = 3
G[4][0] = 2
G[5][1] = 5
t = 1
print(BFS(G, 2, 5, t))
