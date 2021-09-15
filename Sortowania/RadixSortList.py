# Z WARTOWNIKIEM!!!

class Node:
    def __init__(self):
        self.val = 0
        self.next = None

def add_end(head, x):
    a = Node()
    a.val = x
    a.next = None
    p = head

    while p.next != None:
        p = p.next
    p.next = a

def add_begin(head, x):
    a = Node()
    a.val = x
    a.next = None
    p = head
    a.next = p.next
    p.next = a

def get(list):
    res = list.next
    list.next = res.next
    res.next = None
    return res

def wypisz(first):
   p = first.next
   while p is not None:
       print(p.val, end= ' ')
       p = p.next

def empty(head):
    return head.next==None

def CountingSort(list, cyfra, maks, n):
    C = [0]*(maks+1) #tablica licznikow elementow listy
    while not empty(list):
        k = get(list)
        liczba = k.val // cyfra
        r = liczba % 10
        C[r] += 1

    print("C ", C)
    print("lista")
    wypisz(list)
    print()

    j = maks
    while j >= 0:
        if C[j] != 0:
            C[j] -= 1
            add_begin(list, j)
        else:
            j -= 1

def radix_sort(list):
    # szukam maksymalnej liczby zeby znac maksymalna dlugosc liczb
    k = list.next
    maks = 0
    # szukam max w liscie, zeby znac maksymalna dlugosc liczb (przyda mi sie tez zeby znac rozmiar tablicy C), i przy okazji wyliczam rozmiar listy
    while k != None:
        n += 1
        if k.val > maks:
            maks = k.val
        k = k.next
    print("max:", maks, "len: ", n)
    cyfra = 1 #cyfra wg ktorej sortuje (1-jednosci, 10-dziesiatki,...)
    while(maks > 1):
        CountingSort(list, cyfra, maks, n)
        maks = maks // cyfra
        cyfra *= 10