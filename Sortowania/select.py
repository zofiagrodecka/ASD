def partition(tab,p,k):
    x = tab[k]
    i = p-1
    for j in range(p, k):
        if tab[j] <= x:
            i += 1
            tab[i], tab[j] = tab[j], tab[i]
    tab[k], tab[i+1] = tab[i+1], tab[k]
    return i+1


#szukam k-tej co do wielkosci wartosci
def select(tab,p, r, k):
    if p == r:
        return tab[p]
    q = partition(tab,p,r)
    i = q-p+1  # liczba elementow od pozycji p do q wlacznie
    if i == k:
        return tab[q]
    elif k < i:
        return select(tab,p,q-1,k)
    else:
        return select(tab,q+1,r,k-i)


def median(A):
    n = len(A)
    if n % 2 == 1:
        return select(A, 0, n-1, n//2 + 1)
    return (select(A, 0, n-1, n//2) + select(A, 0, n-1, n//2 + 2))/2


tab = [1, 6, 3, 2, 4, 4]
print(select(tab, 0, 4, 3))
print(median(tab))
