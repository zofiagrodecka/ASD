# Z WARTOWNIKIEM!!!

class Node:
    def __init__(self):
        self.val = 0
        self.next = None

def add(head, x):
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

def empty(head):
    return head.next==None

def wypisz(first):
   p = first.next
   while p is not None:
       print(p.val, end= ' ')
       p = p.next


def insertion_sort(tab):
    for i in range(1, len(tab)):
        tmp = tab[i]
        ind = i-1
        while ind >= 0 and tmp < tab[ind]:
            tab[ind+1] = tab[ind]
            ind -= 1
        tab[ind+1] = tmp

def Bucket_Sort(list):
    k = list.next
    maks = list.next.val
    n = 0
    # szukam max w liscie, zeby znac rozmiar tablicy C, i przy okazji wyliczam rozmiar listy
    while k != None:
        n += 1
        if k.val > maks:
            maks = k.val
        k = k.next
   # print("max:", maks, "len: ", n)
    buckets = [None]*n
    for i in range(n):
        buckets[i] = []
    while not empty(list):
        k = get(list)
        normalised = k.val/maks
        buck_ind = int(n*normalised)
        if normalised == 1:
            buck_ind = buck_ind - 1
        buckets[buck_ind].append(k.val)
        #print(buckets)
    #print("buckets: ", buckets)
    for i in range(n):
        insertion_sort(buckets[i])

    i = n-1
    j = len(buckets[i]) - 1
    while i >= 0:
        if j>=0:
            add_begin(list, buckets[i][j])
            buckets[i].pop()
            j -= 1
        else:
            i -= 1
            j = len(buckets[i]) - 1


list = Node()
tab = [1, 3.9, 1.2, 0.8, 1.7, 0.19, 1.3, 0.1, 2.4, 0.12]
for i in range(len(tab)):
    add(list, tab[i])
wypisz(list)
print()
Bucket_Sort(list)
wypisz(list)