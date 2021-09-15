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
    visited[u] = True
    for v in G[u]:
        if not visited[v]:
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
    S.wypisz()
    #return (visited, parent, czasy)


G = [[2, 4, 1],
    [2, 3],
    [],
    [6,5],
    [3],
    [],
    []]
sort_top(G)
print()
