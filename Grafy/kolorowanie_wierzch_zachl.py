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

def BFS(G, s, D):
    n = len(G)
    visited = [False]*n  # list of visited
    colours = [None]*n
    parent = [[]]*n
    print(parent)

    Q = Queue()
    visited[s] = True
    colours[s] = 1
    Q.put(s)
    while not Q.is_empty():
        u = Q.get()
        for v in G[u]:
            if colours[v] == None:
                i = 1
                while colours[u] == i:
                    i += 1
                colours[v] = i
                # print(colours)
                visited[v] = True
                parent[v].append(u)
                Q.put(v)
            elif colours[v] == colours[u]:
                i = 1
                for p in parent[v]:
                    while i == colours[u] or colours[p] == i:
                        i += 1
                colours[v] = i
                # print(colours)
                visited[v] = True
                parent[v].append(u)
                Q.put(v)
    return colours

def paint(G, D):
    n = len(G)
    return BFS(G, 0, D)


g=[[1,3,4],[0,2],[1,4],[0,5],[0,2],[3]]
G2 = [
    [1,4],
    [0,4,2,6],
    [1,3,5,6],
    [2,5],
    [6,5,0,1],
    [4,6,2,3],
    [1,2,4,5]
]
print(paint(G2, 4))