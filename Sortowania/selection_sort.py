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


def wypisz(first):
   p = first.next
   while p is not None:
       print(p.val, end= ' ')
       p = p.next

def SelectionSort(list):
    f = list.next
    prev_min = list
    prev = list
    while f.next != None:
        minimum = f
        p = f.next
        prev_p = f
        while p != None:
            if p.val < minimum.val:
                prev_min = prev_p
                minimum = p
            prev_p = p
            p = p.next
        if minimum == f: #nie trzeba nic zamieniac
            prev = f
            f = f.next
        else:
            last = minimum.next
            prev.next = minimum
            if f == prev_min:
                minimum.next = f
            else:
                prev_min.next = f
                minimum.next = f.next
            f.next = last
            prev = prev.next
            f = prev.next


def Selection_sort(tab):
    n = len(tab)
    for i in range(n):
        ind_min = i
        for j in range(i+1, len(tab)):
            if tab[j] < tab[ind_min]:
                ind_min = j
        tab[ind_min], tab[i] = tab[i], tab[ind_min]


arr = [1, 6, 20, 5, 12, 8]
head = Node()
for i in range(len(arr)):
    add(head,arr[i])
SelectionSort(head)
wypisz(head)
print()