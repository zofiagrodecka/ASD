from random import randrange

def partition(tab, p, k):
    x = tab[k]
    i = p-1
    for j in range(p, k):
        if tab[j] <= x:
            i += 1
            tab[i], tab[j] = tab[j], tab[i]
    tab[i+1], tab[k] = tab[k], tab[i+1]
    return i+1

def QuickSort(tab, p, k):
    if p < k:
        q = partition(tab, p, k)
        QuickSort(tab, p, q-1)
        QuickSort(tab, q+1, k)


tab = [2, 3, 1, 0, 5, 2, 3, 2]
QuickSort(tab, 0, len(tab)-1)
print(tab)

"""def randpartition(tab, p, k):
    s = randrange(p, k+1)
    tab[s], tab[k] = tab[k], tab[s]
    return partition(tab, p ,k)"""