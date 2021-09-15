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
        return res.val

    def wypisz(self):
        p = self.head.next
        while p is not None:
            print(p.val, end=' ')
            p = p.next

def BFS(G,s):
    n = len(G)
    distance = [None] * n
    visited = [False] * n
    parent = [-1] * n

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
    # print("parent: ", parent)
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
    F = [[0 for j in range(n)] for i in range(n)]  # nasze plywy
    global end
    while not end:
        path = []
        extension = find_argumenting_path(residual, s, t)
        if end:
            break
        # print("extension: ", extension)
        if extension > 0:
            f += extension
            # print(path)
            for i in path:
                if i[0] != -1:
                    if c[i[0]][i[1]] > 0:  # krawedz z argumenting path istnieje w naszym oryginalnym grafie
                        F[i[0]][i[1]] += extension
                    elif c[i[0]][i[1]] == 0:
                        F[i[1]][i[0]] = 0
                    residual[i[0]][i[1]] = c[i[0]][i[1]] - F[i[0]][i[1]]
                    residual[i[1]][i[0]] = F[i[0]][i[1]]
                    # print(F, residual)
    return f


"""c = [[0 for j in range(4)] for i in range(4)]
c[0][1] = 2
c[0][2] = 1
c[1][2] = 1
c[1][3] = 1
c[2][3] = 2
#print("c ", c)
print( max_flow( c, 0, 3 ) ) # wypisze 3 """

"""C2 = [[0 for j in range(7)] for i in range(7)]
C2[0][1] = 7
C2[0][3] = 3
C2[1][3] = 4
C2[1][4] = 6
C2[2][0] = 9
C2[2][5] = 9
C2[3][4] = 9
C2[3][6] = 2
C2[5][3] = 3
C2[5][6] = 6
C2[6][4] = 8
print(max_flow(C2, 2, 4))"""

C3 = [[0 for j in range(8)] for i in range(8)]
C3[0][1] = 1
C3[0][2] = 1
C3[0][3] = 1
C3[1][4] = 5
C3[1][5] = 5
C3[1][6] = 5
C3[2][5] = 5
C3[2][6] = 5
C3[3][6] = 5
C3[6][7] = 3
C3[5][7] = 2
C3[4][7] = 1
print(max_flow(C3, 0, 7))