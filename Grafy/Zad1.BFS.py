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


def BFS(G,s):
    n = len(G)
    visited = [False] * n  # tablica odwiedzonych
    result = [None] * n #tablica list [parent, distance]
    for i in range(n):
        result[i] = [0]*2

    Q = Queue() #kolejka
    result[s][1] = 0
    visited[s] = True
    result[s][0] = None
    Q.put(s)
    while not Q.is_empty():
        u = Q.get()
        for v in range(n): #dla kazdego wierzcholka w grafie
            if G[u][v] == 1 and not visited[v]: #jesli istnieje krawedz z wierzcholka u do wierzcholka v i v nie byl odwiedzony
                visited[v] = True
                result[v][1] = result[u][1] + 1
                result[v][0] = u
                Q.put(v)
    for i in range(n): #zamieniam listy w result na krotki
        result[i] = tuple(result[i])
    return result


# elementarny test, powinien wypisać
# [(None,0), (0,1), (0,1), (2,2)]
# lub
# [(None,0), (0,1), (0,1), (1,2)]
G = [[0,1,1,0],[0,0,0,1],[0,1,0,1], [0,0,0,0]]
print( BFS(G,0) )
#moj test - graf z wykladu do implementacji BFS
graf = [[0, 1, 1, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 1, 1, 0], [0, 0, 0, 1, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0,0,0,0,0,0,0,0]]
print(BFS(graf,0))
