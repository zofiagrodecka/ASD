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


def BFS(G,s):
    n = len(G)
    distance = [10000] * n  # list of distances
    parent = [None] * n  # list of parents
    visited = [False]*n

    Q = Queue()
    parent[s] = None
    distance[s] = 0
    Q.put((s, 0))  # number of vertex, weight of edge - 1
    while not Q.is_empty():
        u, weight = Q.get()
        if not visited[u]:
            if weight == 0:
                visited[u] = True
                for v in range(n):
                    if G[u][v] > 0 and distance[v] > distance[u] + G[u][v]:
                        distance[v] = distance[u] + G[u][v]
                        parent[v] = u
                        Q.put((v, G[u][v] - 1))
            else:
                Q.put((u, weight-1))
        """print("queue: ")
        Q.wypisz()
        print()"""
    return distance, parent


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
print(BFS(G, 0))
