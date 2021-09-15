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


def InsertionSort(list):
    prev = list
    current = list.next
    while current != None:
        print("current: ", current.val)
        p = list.next
        p_prev = list
        while p.val < current.val:
            p_prev = p
            p = p.next
        #p_prev wskazuje na poprzednika tego gdzie ma trafic current
        print("prev, p: ",p_prev.val,  p.val)
        if p.val != current.val:
            p_prev.next = current
            prev.next = current.next
            current.next = p
            current = prev.next
        else:
            prev = current
            current = current.next
        wypisz(list)
        print()


def insertion_sort(tab):
    for i in range(1, len(tab)):
        tmp = tab[i]
        ind = i-1
        while ind >= 0 and tmp < tab[ind]:
            tab[ind+1] = tab[ind]
            ind -= 1
        tab[ind+1] = tmp


arr = [170, 45, 75, 90, 802, 24, 2, 66]
"""insertion_sort(arr)
print("ARR: " , arr)"""

head = Node()
for i in range(len(arr)):
    add(head,arr[i])
InsertionSort(head)
wypisz(head)
print()