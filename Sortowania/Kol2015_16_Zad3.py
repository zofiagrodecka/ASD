# Proszę zaimplementować funkcję któa otrzymuje na wejściu listę jednokierunkową bez wartownika. 
# Lista ta jest prawie posortowana w tym sensie, że powstała z listy posortowanej przez zmianę 1 losowo wybranego 
# elementu na losową wartość. Funkcja powinna przepiąć elementy tak, by lista stała się posortowana i zwrócić wskaźnik 
# do głowy tej listy.


class Node:
    def __init__(self):
        self.val = 0
        self.next = None

def add(head, x):
    a = Node()
    a.val = x
    a.next = None
    p = head

    if p == None:
        p = a
    else:
        while p.next != None:
            p = p.next
        p.next = a


def wypisz(first):
   p = first.next
   while p is not None:
       print(p.val, end= ' ')
       p = p.next

def fixSortedList(L):
    p = L
    prev = None
    while p.next.val >= p.val:
        prev = p  # poprzednik p
        p = p.next
    #p wskazuje na element w zlym miejscu

    #usuwamy element niepasujacy z listy
    if prev == None: # niepasujacy jest pierwszy w liscie
        L = L.next
    else:
        prev.next = p.next
    p.next = None
    #idziemy od poczatku listy i szukamy miejsca dla niepasujacego elementu (p)
    q = L
    prev = None #poprzednik q
    while q != None and q.val < p.val:
        prev = q
        q = q.next
    #wstawiam p w odpowiednie miejsce
    if q == L: #jesli p ma byc 1 w liscie
        L = p
    else:
        prev.next = p
    p.next = q
    return L


head = Node()
arr = [1, 4, 6, 10, 9]
for i in range(len(arr)):
    add(head,arr[i])
wypisz(fixSortedList(head))

