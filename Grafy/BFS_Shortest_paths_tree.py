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
    shortest_paths_tree = [[] for _ in range(n)]
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
                shortest_paths_tree[u].append(v)
                shortest_paths_tree[v].append(u)
                parent[v] = u
                Q.put(v)
    return shortest_paths_tree


graf = [[1, 2], [2], []]
G = [[1, 3],
    [0, 2],
    [1, 3],
    [0, 4],
    [3]]
print(BFS_lista(G, 0))