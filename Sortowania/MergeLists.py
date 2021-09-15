class Node:
    def __init__(self):
        self.val = 0
        self.next = None

def add(head, x):
    a = Node()
    a.val = x
    a.next = None
    p = head

    if head == None:
        head = a
    else:
        while p.next != None:
            p = p.next
        p.next = a
    return head

def wypisz(first):
   p = first
   while p is not None:
       print(p.val, end= ' ')
       p = p.next

def Merge(List1, List2):
    p = List1
    q = List2
    res = None
    end = None
    if p.val <= q.val:
        res = p
        end = p
        List1 = p.next
        p.next = None
        p = List1
    else:
        res = q
        end = q
        List2 = q.next
        q.next = None
        q = List2

    while p != None and q != None:
        if p.val <= q.val:
            end.next = p
            List1 = p.next
            p.next = None
            end = end.next
            p = List1
        else:
            end.next = q
            end = end.next
            List2 = q.next
            q.next = None
            q = List2

    if p != None:
        end.next = p
    if q != None:
        end.next = q
    return res


L1 = None
L2 = None
tab = [1,2,3,4,5]
tab2= [1, 5, 6, 7]
for i in range(len(tab)):
    L1 = add(L1, tab[i])
for i in range(len(tab2)):
    L2 = add(L2, tab2[i])
wypisz(Merge(L1,L2))