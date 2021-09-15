def partition_last(tab,p,k): #partition zwracajaca indeks ostatniego wystapienia elementu wg ktorego dzielilismy
    x = tab[p]
    i = p
    for j in range(p+1,k+1):
        if tab[j] <= x:
            i += 1
            tab[i], tab[j] = tab[j], tab[i]
    tab[p], tab[i] = tab[i], tab[p]
    return i


def partition_first(tab,p,k): #funkcja zwracajaca indeks pierwszego wystapienia elementu wg ktorego dzielilismy
    x = tab[k]
    i = p-1
    for j in range(p, k):
        if tab[j] < x:
            i += 1
            tab[i], tab[j] = tab[j], tab[i]
    tab[k], tab[i+1] = tab[i+1], tab[k]
    return i+1


def quickersort(tab, p, k):
    if p < k:
        last = partition_last(tab, p, k)
        first = partition_first(tab, p, last)
        quickersort(tab, p, first-1) #sortuje polowe tablicy z mniejszymi elementami
        quickersort(tab, last+1, k) #sortuje polowe tablicy z wiekszymi elementami


A = [10, 6, 10, 100, 15, 20, 30, 9, 21]
quickersort(A, 0, 8)
print(A)