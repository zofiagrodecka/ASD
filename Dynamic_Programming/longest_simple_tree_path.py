class Node:
    def __init__( self ):
        self.children = 0 # liczba dzieci węzła
        self.child = [] # lista par (dziecko, waga krawędzi)
        self.path_length = None
        self.parent = None


def heavy_path(T):
    tmp = T
    prev = None
    while tmp.children > 0:
        prev = tmp
        tmp = tmp.child[0]
        tmp.parent = prev
    while prev != T:
        prev.path_length = prev.child[0][0].path_length + prev.child[0][1]
        for i in range(1, len(prev.child)):
            kid, weight = prev.child[i]
            if kid.path_length == None:
                kid.path_length = 0
            if kid.path_length + weight > prev.path_length:
                prev.path_length = kid.path_length + weight



A = Node()
B = Node()
C = Node()
A.children = 2
A.child = [ (B,5), (C,-1) ]
