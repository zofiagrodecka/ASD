class Node:
    def __init__(self):
        self.parent = None
        self.G = None
        self.A = None
        self.T = None
        self.C = None
        self.visited = False

class Tree:
    def __init__(self):
        self.root = Node()

    def insert(self, string):
        n = len(string)
        tmp = self.root
        for i in range(n-1):
            if string[i] == 'G':
                if tmp.G == None:
                    tmp.G = Node()
                    tmp.G.parent = tmp
                tmp = tmp.G
            if string[i] == 'A':
                if tmp.A == None:
                    tmp.A = Node()
                    tmp.A.parent = tmp
                tmp = tmp.A
            if string[i] == 'T':
                if tmp.T == None:
                    tmp.T = Node()
                    tmp.T.parent = tmp
                tmp = tmp.T
            if string[i] == 'C':
                if tmp.C == None:
                    tmp.C = Node()
                    tmp.C.parent = tmp
                tmp = tmp.C
        if string[n-1] == 'G':  # zaznaczam że to koniec napisu (visited)
            if tmp.G == None:
                tmp.G = Node()
                tmp.G.parent = tmp
            if tmp.G.visited:
                return False
            tmp.G.visited = True
        if string[n-1] == 'A':
            if tmp.A == None:
                tmp.A = Node()
                tmp.A.parent = tmp
            if tmp.A.visited:
                return False
            tmp.A.visited = True
        if string[n-1] == 'T':
            if tmp.T == None:
                tmp.T = Node()
                tmp.T.parent = tmp
            if tmp.T.visited:
                return False
            tmp.T.visited = True
        if string[n-1] == 'C':
            if tmp.C == None:
                tmp.C = Node()
                tmp.C.parent = tmp
            if tmp.C.visited:
                return False
            tmp.C.visited = True
        return True


def different(tab):
    T = Tree()
    for string in tab:
        if not T.insert(string):
            return False
    return True


tab = ["ATTC", "ATGC", "ATTCG", "ATGC"]
if different(tab):
    print("Ok")
else:
    print("Sa powtorzenia")