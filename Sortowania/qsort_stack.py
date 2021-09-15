class Node:
    def __init__(self):
        self.val1 = None
        self.val2 = None
        self.next = None

class Stack:
    def __init__(self):
        self.top = Node()

    def push(self, x, y):
            N = Node()
            N.val1 = x
            N.val2 = y
            N.next = self.top.next
            self.top. next = N

    def pop(self):
        N = self.top.next
        self.top.next = N.next
        return N.val1, N.val2

    def is_empty(self):
        if self.top.next != None:
            return False
        return True

    def wypisz(self):
        p = self.top.next
        while p is not None:
            print(p.val1, p.val2)
            p = p.next


def partition(tab, p, k):
    x = tab[k]
    i = p-1
    for j in range(p, k):
        if tab[j] <= x:
            i += 1
            tab[i], tab[j] = tab[j], tab[i]
    tab[i+1], tab[k] = tab[k], tab[i+1]
    return i+1

def QuickSort(tab, p, k):
    s = Stack()
    s.push(p,k)
    while not s.is_empty():
        i, j = s.pop()
        q = partition(tab,i,j)
        if q-1 > i:
            s.push(i, q-1)
        if q+1 < j:
            s.push(q+1, j)


tab = [2, 3, 1, 0, 5, 2, 3, 2]
QuickSort(tab, 0, len(tab)-1)
print(tab)

