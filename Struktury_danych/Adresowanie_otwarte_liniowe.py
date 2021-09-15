#STATES:
FREE = 0
TAKEN = 1
KEEP_LOOKING = 2

class elem:
    def __init__(self):
        self.key = ''  # klucz
        self.value = ''  # wartosc
        self.state = 0

"""def h(x, n, i):
    j = 0
    k = 0
    for j in range(len(x)):
        k += ord(x[j])
        j += 1
    return (k+i) % n  # a == 0"""

def h(key, n, i):
    v = int('0b10101010', 2)
    for l in key:
        v ^= ord(l) % 255

    return (v+i) % n

def insert(tab, x, y):  # pod klucz x wstaw wartosc y
    n = len(tab)
    global TAKEN

    k = h(x, n, 0)  # pierwotny indeks (klucz)

    new = elem()
    new.key = x
    new.value = y

    attempt = 0
    while tab[k].state == TAKEN:  # dopoki nie znalazlam wolnego miejsca
        attempt += 1
        k = h(x,n,attempt)
    tab[k] = new
    tab[k].state = TAKEN

def find(tab, x):
    n = len(tab)
    global FREE
    global TAKEN
    global KEEP_LOOKING

    k = h(x, n, 0)
    attempt = 0
    # dopoki nie znalazlam danego elementu albo nie natrafilam na pole, ktore jeszcze nigdy nie bylo zajete
    while (tab[k].state == TAKEN or tab[k].state == KEEP_LOOKING) and (tab[k].key != x):
        attempt += 1
        k = h(x, n, attempt)
    if tab[k].state != TAKEN:  # znalazlam pole FREE
        return None
    else:
        return tab[k].value

def remove(tab, x):
    n = len(tab)
    global FREE
    global TAKEN
    global KEEP_LOOKING

    k = h(x, n, 0)
    # print("first key: ", k)
    attempt = 0
    while (tab[k].state == TAKEN or tab[k].state == KEEP_LOOKING) and tab[k].key != x:
        attempt += 1
        # print("attempt: ", attempt)
        k = h(x, n, attempt)
        # print(k)
    if tab[k].state == TAKEN:  # znalazlam
        tab[k].state = KEEP_LOOKING
        tab[k].value = ''
        tab[k].key = ''

def wypisz(tab):
    n = len(tab)
    global TAKEN
    for i in range(n):
        print("index: ", i, end=' ')
        if tab[i].state == TAKEN:
            print(tab[i].key, tab[i].value)
        else:
            if tab[i].state == 0:
                print("free")
            if tab[i].state == 2:
                print("keep_looking")


n = 20
m = 5
tab = [elem()]*n
insert(tab, "Piotr", "Piotr")
insert(tab, "Ala", "Ala")
insert(tab, "kot", "kot")
insert(tab, "Michal", "Michal")
insert(tab, "Zosia", "Zosia")
wypisz(tab)
remove(tab,"Piotr")
remove(tab, "Ala")
wypisz(tab)
print(find(tab,"Michal"))
print(find(tab, "Piotr"))
print(find(tab, "Ala"))
