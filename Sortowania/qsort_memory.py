def partition(tab,p,k):
    x = tab[k]
    i = p-1
    for j in range(p, k):
        if tab[j] <= x:
            i += 1
            tab[i], tab[j] = tab[j], tab[i]
    tab[k], tab[i+1] = tab[i+1], tab[k]
    return i+1

def quicksort(A, i, j):
    while i<j:
        k = partition(A, i, j)
        if k-i < j-k:
            quicksort(A, i, k-1)
            i = k+1
        else:
            quicksort(A, k+1, j)
            j = k-1


tab = [ 1, 6, 3, 2, 4]
quicksort(tab, 0, len(tab) - 1)
print(tab)