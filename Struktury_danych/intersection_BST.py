class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.parent = None
        self.left = None
        self.right = None

def minimum(root):
    while root.left != None:
        root = root.left
    return root

def maximum(root):
    while root.right != None:
        root = root.right
    return root

def successor(x):
    if x.right != None:
        return minimum(x.right)
    p = x.parent
    while p != None and x == p.right:  # dopoki x jest prawym synem
        x = x.parent
        p = p.parent
    return p  # p == x.parent

def predecessor(x):
    if x.left != None:
        return maximum(x.left)
    p = x.parent
    while p != None and x == p.left:
        x = x.parent
        p = p.parent
    return p

class BSTDict:
    def __init__(self):
        self.tree = None  # tu powinien być korzeń drzewa gdy slownik nie jest pusty

    def find(self, key):
        root = self.tree
        while root != None:
            if root.key == key:
                return root
            elif root.key < key:
                root = root.right
            else:
                root = root.left
        return None

    def insert(self, key, value):  # wstaw wartość value pod klucz key (jeśli klucz key już istnieje, to podmień przechowywaną wartość value)
        node = BSTNode(key, value)
        if self.tree == None:
            self.tree = node
            return
        else:
            f = self.find(key)
            if f == None:
                x = self.tree
                while x != None:
                    p = x  # parent
                    if node.key < x.key:
                        x = x.left
                    else:
                        x = x.right
                node.parent = p
                if node.key < p.key:
                    p.left = node
                else:
                    p.right = node
            else:
                f.value = value  # podmieniam wartość
            return

    def transplant(self, u, v): # zastępuję węzeł u, węzłem v
        if u.parent == None:  # root drzewa
            self.tree = v
        elif u == u.parent.left:  # u jest lewym synem
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent

    def remove(self, key):  # usuń z drzewa węzeł z kluczem key
        x = self.find(key)
        print(x.key)
        if x.left == None:  # x nie ma lewego dziecka
            self.transplant(x, x.right)  # zastepuje go prawym poddrzewem (albo Nonem)
        elif x.right == None:  # x nie ma prawego dziecka
            self.transplant((x, x.left))  # zastepuje go lewym poddrzewem
        else:
            succ = successor(x)
            if succ.parent != x:  # nastepnik nie jest dzieckiem x
                self.transplant(succ, succ.right)
                succ.right = x.right
                succ.right.parent = succ
            self.transplant(x, succ)
            succ.left = x.left
            succ.left.parent = succ


def printBST(root):
    if root == None:
        return
    printBST(root.left)
    print(root.key, root.value)
    printBST(root.right)


def intersection(T1, T2):
    x = minimum(T1.tree)
    y = minimum(T2.tree)
    licz = 0
    while x != None and y != None:
        if x.key == y.key:
            licz += 1
            x = successor(x)
            y = successor(y)
        elif x.key < y.key:
            x = successor(x)
        else:
            y = successor(y)
    return licz


Tree1 = BSTDict()
root = BSTDict()
# print(root.tree.key)
root.insert(10, "Ala")
root.insert(5, "ma")
root.insert(2, "kota")
root.insert(4, "a")
root.insert(20, "kot")
root.insert(25, "ma")
root.insert(15, "ale")
root.insert(12, "i")
root.insert(17, "razem")
root.insert(22, "sie")
root.insert(21, "swietnie")
root.insert(24, "bawia")
root.insert(27, "tak!")

Tree1.insert(10, "Ala")
Tree1.insert(5, "ma")
Tree1.insert(20, "kot")
Tree1.insert(24, "bawia")
Tree1.insert(27, "tak!")
print(intersection(Tree1, root))
