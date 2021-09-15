# Dana jest tablica n elementowa zawierająca liczby naturalne. Wiadomo, że ta tablica powstała w 2 krokach. 
# Najpierw wygenerowano losowo (z nieznanym rozkładem) n różnych liczb nieparzystych i posortowano je rosnaco. 
# Następnie wybrano losowo ceil z logn elementów powstałej tablicy i zamieniono je na losowo wybrane liczby parzyste. 
# Zaproponuj algorytm sortowania tak powstałych danych.

from math import ceil, log2

def Merge(tab, p, sr, k):
    T = [0]*(k+1)
    l = p
    r = sr+1
    i = p
    while l <= sr and r <= k:
        if tab[l] < tab[r]:
            T[i] = tab[l]
            l += 1
        else:
            T[i] = tab[r]
            r += 1
        i+=1
    if l <= sr:
        for j in range(i, k+1):
            T[j] = tab[l]
            l += 1
    if r <= k:
        for j in range(i, k+1):
            T[j] = tab[r]
            r += 1

    for j in range(p, k+1):
        tab[j] = T[j]


def MergeSort(tab, p, k):
    if p != k:
        sr = (p+k)//2
        MergeSort(tab, p, sr)
        MergeSort(tab, sr+1, k)
        Merge(tab, p, sr, k)
    return


def Merge_odd_even(A, even):
    n = len(A)
    m = len(even)
    l = 0
    r = 0
    res = [0]*(n)
    i = 0
    while l<n and r<m:
        if A[l] % 2 != 0:  # liczba nieparzysta
            if A[l] <= even[r]:
                res[i] = A[l]
                l += 1
            else:
                res[i] = even[r]
                r += 1
            i += 1
        else:
            l += 1

    if l<n:
        for j in range(i, n):
            res[j] = A[l]
            l += 1
    if r<m:
        for j in range(i, n):
            res[j] = even[r]
            r += 1
    return res


def sort(A):
    n = len(A)
    even = [0]*ceil(log2(n))
    j = 0
    for i in range(n):
        if A[i]%2 == 0:  # liczba jest parzysta
            even[j] = A[i]
            j += 1
    print(even)
    MergeSort(even, 0, len(even) - 1)
    print(even)
    return Merge_odd_even(A, even)


tab = [1, 2, 3, 100, 9, 98, 99]
print(sort(tab))