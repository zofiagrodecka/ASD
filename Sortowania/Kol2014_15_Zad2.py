# Napisz funkcję, która rozdziela listę na 2: jedną zawierającą liczby parzyste a drugą zawierającą liczby nieparzyste.

#bez wartownika
class Node:
    def __init__(self):
        self.val = 0
        self.next = None

class TwoLists:
    def __init__(self):
        self.even = None
        self.odd = None


def add_end(head, x):
    a = Node()
    a.val = x
    a.next = None
    p = head

    if p == None:
        head = a
    else:
        while p.next != None:
            p = p.next
        p.next = a
    return head


def add(head, x):
    a = Node()
    a.val = x
    a.next = head
    head = a
    return head

def get(list): #tylko usuwa 1 element listy
    p = list
    list = list.next
    p.next = None
    return list

def empty(list):
    return list==None

def wypisz(first):
   p = first
   while p is not None:
       print(p.val, end= ' ')
       p = p.next

def printTwo(x):
    wypisz(x.odd)
    print()
    wypisz(x.even)


def TwoListsSplit(list):
    result = TwoLists()
    while not empty(list):
        x = list.val
        list = get(list)
        if x % 2 == 0:
            result.even = add(result.even, x)
        else:
            result.odd = add(result.odd, x)
    return result


list = None
tab = [2, 3, 1, 0, 5, 2, 3, 2]
for i in range(len(tab)):
    list = add_end(list, tab[i])
wypisz(list)
print()
printTwo(TwoListsSplit(list))
