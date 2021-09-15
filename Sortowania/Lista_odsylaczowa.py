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