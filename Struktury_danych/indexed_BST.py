class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.parent = None
        self.left = None
        self.right = None
        self.subtree_size = 0

def minimum(root):
    while root.left != None:
        root= root.left
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
                    p.subtree_size += 1
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
                f.value = value  # podmieniam wartość juz istniejacego wezla

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

    def select(self, i):
        x = self.tree
        while x.left != None and x.left.subtree_size + 2 != i:
            if x.left.subtree_size + 2 < i:  # szukamy na prawo
                i = i - x.left.subtree_size - 2
                x = x.right
            else:
                x = x.left
        return x

    def in_which_subtree(self, key):
        x = self.tree
        res = 0
        while x.key != key:
            if x.key > key:  # idziemy na lewo
                x = x.left
            else:
                res = res + x.left.subtree_size + 2
                x = x.right
        res += x.left.subtree_size + 2
        return res


def printBST(root):
    if root == None:
        return
    printBST(root.left)
    print(root.key, root.value, root.subtree_size)
    printBST(root.right)


root = BSTDict()
a = 13
r = 5
f = 5

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
printBST(root.tree)
k = root.select(12).key
print(k)
print(root.in_which_subtree(k))