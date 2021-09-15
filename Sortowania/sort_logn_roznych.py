from math import log2

def BinarySearch(tab, p, k, el):
    if p <= k:
        sr = p + (k-p)//2
        if el == tab[sr][0]:
            return True, sr
        elif el < tab[sr][0]:
            return BinarySearch(tab, p, sr-1, el)
        else:
            return BinarySearch(tab, sr+1, k, el)
    return False, p

def sort(A):
    n = len(A)
    # tablica B zawiera unikatowe liczby z A
    B = [None] * int(log2(n))  # B = [[wartosc, ilosc_wystapien], [wart, il_wyst], ...]
    sizeB = 0  # ilosc elementow w B
    for i in range(int(log2(n))):
        B[i] = [-1] * 2
    for x in range(n):
        found, i = BinarySearch(B, 0, sizeB-1, A[x])
        if found:
            B[i][1] += 1
        else:
            sizeB += 1
            for j in range(sizeB-1, i, -1):
                B[j] = B[j-1]
            tmp = [A[x], 1]
            B[i] = tmp
    k = 0
    for i in range(n):
        A[i] = B[k][0]
        B[k][1] -= 1
        if B[k][1] == 0:
            k += 1
    return A


tab = [5.4, 2.5, 5.4, 7.0, 5.4, 7.0, 2.5, 7.0 ]
print(sort(tab))