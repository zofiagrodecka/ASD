class node:
    def __init__(self):
        self.value = ''
        self.next = None

"""def h(x, n):
    j = 0
    k = 0
    for j in range(len(x)):
        k += ord(x[j])
        j += 1
    return k % n"""


def h(key, n):
    v = int('0b10101010', 2)
    for l in key:
        v ^= ord(l) % 255

    return v % n

def insert(tab, x):  # pod kluczem k wstaw x
    n = len(tab)
    new = node()
    new.value = x
    k = h(x, n)
    if tab[k] == None:
        tab[k] = new
    else:
        new.next = tab[k]
        tab[k] = new

def find(tab, x):
    n = len(tab)
    k = h(x, n)
    if tab[k] == None:  # nie ma elementu
        return None
    else:
        p = tab[k]
        while p != None and p.value != x:  # dopoki nie znalazlam
            p = p.next

        if p == None:  # nie ma elementu
            return None
        else:  # znalazlam
            return k

def remove(tab, x):
    n = len(tab)
    k = h(x, n)
    if tab[k] != None:  # cos jest pod tym indeksem
        p = tab[k]
        prev = None
        while p != None and p.value != x:  # dopoki nie znalazlam
            prev = p
            p = p.next
        if prev == None:  # trzeba usunac glowe listy
            tab[k] = p.next
        else:
            prev.next = p.next

def wypisz(tab):
    for i in range(len(tab)):
        if tab[i] != None:
            p = tab[i]
            print("index: ", i, end=' ')
            while p != None:
                print(p.value, end=' ')
                p = p.next
            print()


n = 6
tab = [None]*n
insert(tab, "Piotr")
insert(tab, "Ala")
insert(tab, "Michal")
insert(tab, "Pawel")
insert(tab, "Zosia")
wypisz(tab)
remove(tab,"Piotr")
remove(tab, "Ala")
print("once again")
wypisz(tab)
print(find(tab,"Michal"))
print(find(tab, "Piotr"))