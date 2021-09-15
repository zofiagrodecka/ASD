from math import log2

def bubble_sort(tab):
    n = len(tab)
    for i in range(0,n-1):
        for j in range(0, n-i-1):
            if tab[j][0] > tab[j+1][0]:
                tab[j][0], tab[j+1][0] = tab[j+1][0], tab[j][0]
    return tab

def sort(A):
    n = len(A)
    #tablica B zawiera unikatowe liczby z A
    B = [None]*int(log2(n)) # B = [[wartosc, ilosc_wystapien], [wart, il_wyst], ...]
    for i in range(int(log2(n))):
        B[i] = [0]*2
    sizeB = 0 #ilosc elementow w B
    for i in range(n):
        found = False
        for j in range(sizeB):
            if B[j][0] == A[i]:
                found = True
                B[j][1] += 1
        if not found:
            B[sizeB][0] = A[i]
            B[sizeB][1] += 1
            sizeB += 1
    print(B)
    B = bubble_sort(B)
    print(B)
    j = 0  # indeks rozpatrywanego elementu w B
    for i in range(n):
        A[i] = B[j][0]
        B[j][1] -= 1
        if B[j][1] == 0:
            j += 1
    return A


tab = [5.4, 2.5, 5.4, 7.0, 5.4, 7.0, 2.5, 7.0 ]
print(sort(tab))