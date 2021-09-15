class Node:
    def __init__(self):
        self.val = 0
        self.next = None

def add(head, x):
    a = Node()
    a.val = x
    a.next = None

    app(head, a)


def app(head, elem): #head = [first, last]
    if head[0] == None:
        head[0] = elem
    else:
        head[1].next = elem
    head[1] = elem

def get(head): #usuwam pierwszy element listy
    res = head[0]
    head[0] = head[0].next
    res.next = None
    return res

def empty(head):
    return head[0]==None

def wypisz(head):
   p = head[0]
   while p is not None:
       print(p.val, end= ' ')
       p = p.next


def concatenate(list1, list2):
    if list1[0] == None:
        return list2
    if list2[0] == None:
        return list1
    first = list1[0]
    list1[1].next = list2[0]
    last = list2[1]
    return [first, last]



def QuickSort(list):
    if empty(list):
        return list
    x = list[0].val #porownuje z pierwszym w partition
    smaller = [None, None]
    equal = [None, None]
    greater = [None, None]
    while not empty(list):
        tmp = get(list)
        if tmp.val < x:
            app(smaller,tmp)
        elif tmp.val == x:
            app(equal,tmp)
        else:
            app(greater, tmp)
    return concatenate(concatenate(QuickSort(smaller), equal), QuickSort(greater))


tab = [2, 3, 1, 0, 5, 2, 3, 2]
lista = [None, None]  # wskazania na 1 i ostatni element
for i in range(len(tab)):
    add(lista, tab[i])
wypisz(lista)
print()
wypisz(QuickSort(lista))

