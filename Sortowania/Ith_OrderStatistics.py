def partition(tab,p,k):
    x = tab[k]
    i = p-1
    for j in range(p, k):
        if tab[j] <= x:
            i += 1
            tab[i], tab[j] = tab[j], tab[i]
    tab[k], tab[i+1] = tab[i+1], tab[k]
    return i+1


# funkcja zwraca wartosc elementu, ktory znajdowalby sie pod indeksem i w posortowanej tablicy;
# wszystkie elementy <= od niego sa pod mniejszymi indeksami; wszystkie wieksze pod wiekszymi
def Ith_OrderStatistics(tab, p, k, i):
    q = partition(tab, p, k)
    if i == q:
        return tab[i]
    elif q > i:
        return Ith_OrderStatistics(tab, p, q-1, i)
    else:
        return Ith_OrderStatistics(tab, q+1, k, i)


tab = [ 1, 6, 3, 2, 4]
print(Ith_OrderStatistics(tab, 0, len(tab)-1, len(tab)//2 +1))
print(tab)