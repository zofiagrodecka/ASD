# Proszę zaimplementować funkcję SumSort(A,B). Przyjmuje ona na wejściu 2 n-elementowe tablice (A, B) 
# i zapisuje w B taką permutację elementów z A, że:
# suma od i=0 do n-1 z B[i] <= suma od i=n do 2n-1 z B[i] <= ... <= suma od i=n^2 - n do n^2-1 z B[i].

from math import sqrt

def partition(tab, p, k):
    x = tab[k][0]
    i = p-1
    for j in range(p, k):
        if tab[j][0] <= x:
            i += 1
            tab[i][0], tab[j][0] = tab[j][0], tab[i][0]
    tab[i+1][0], tab[k][0] = tab[k][0], tab[i+1][0]
    return i+1


def QuickSort(tab, p, k):
    if p < k:
        q = partition(tab, p, k)
        QuickSort(tab, p, q-1)
        QuickSort(tab, q+1, k)

def SumSort(A):
    n = len(A)
    B = [0] * n
    sums = [None]*int(sqrt(n))  # tablica list [wartosc sumy, lista liczb wzietych do sumy]
    for i in range(int(sqrt(n))):
        sums[i] = [0]*2
        sums[i][1] = [0]*int(sqrt(n))

    licz = 0  # licze ile zsumowalam elementow
    s = 0  # indeks sumy, ktora teraz liczona
    for i in range(n):
        licz += 1
        sums[s][1][licz-1] = A[i]  # elementy nalezace do s-tej sumy
        sums[s][0] += A[i]  # suma n-elementow
        if sqrt(n) == licz:  # po zsumowaniu n elementow, musze liczyc kolejna sume
            licz = 0
            s += 1
    print(sums)
    QuickSort(sums, 0, len(sums)-1)  # sortuje sumy tylko po 0 polu = po ich wartosci
    # sums.sort(key=fun)
    print(sums)
    licz = 0  # licze ile zsumowalam elementow
    s = 0  # indeks sumy, ktora teraz wypisywana
    for i in range(n):
        licz += 1
        B[i] = sums[s][1][licz-1]  # przepisuje elementy s-tej sumy zeby byly w dobrej czesci tablicy
        if sqrt(n) == licz:
            licz = 0
            s += 1
    return B


tab = [5, 8, 1, 12, 9, 10, 9, 4, 2]
print(SumSort(tab))


