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

def CountingSort(list):
    k = list.next
    maks = list.next.val
    n = 0
    #szukam max w liscie, zeby znac rozmiar tablicy C, i przy okazji wyliczam rozmiar listy
    while k != None:
        n += 1
        if k.val > maks:
            maks = k.val
        k = k.next
    print("max:" , maks,  "len: ", n)
    C = [0]*(maks+1)
    while not empty(list):
        k = get(list)
        C[k.val] += 1

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


def Counting_sort(A):
    k = max(A)  # tablica C bedzie miala taki rozmiar ile wynosi wartosc najwiekszego elementu tablicy A
    print(" Max w tab: ", k)
    n = len(A)
    B = [0]*n
    C = [0]*(k+1)
    for i in range(n):
        C[A[i]] += 1
    for i in range(1,k+1):
        C[i] += C[i-1]
    for i in range(n-1, -1, -1):
        C[A[i]] -= 1
        B[C[A[i]]] = A[i]
    for i in range(n):
        A[i] = B[i]


list = Node()
tab = [2, 3, 1, 0, 5, 2, 3, 2]
CountingSort(tab)
print(tab)
for i in range(len(tab)):
    add_end(list, tab[i])
wypisz(list)
print()
CountingSort(list)
wypisz(list)

