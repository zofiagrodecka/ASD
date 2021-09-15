# Zaimplementuj funkcję SumBetween(T, From, To), która oblicza sumę liczb z n elementowej tablicy T, które
# w posortowanej tablicy znajdywałyby się na pozycjach od indeksach od from do to włącznie.
# O(n)

def partition(tab,p,k):
    x = tab[k]
    i = p-1
    for j in range(p, k):
        if tab[j] <= x:
            i += 1
            tab[i], tab[j] = tab[j], tab[i]
    tab[k], tab[i+1] = tab[i+1], tab[k]
    return i+1

def Ith_Statistics(tab, p, k, i):
    q = partition(tab, p, k)
    if i == q:
        return
    elif q > i:
        Ith_Statistics(tab, p, q-1, i)
    else:
        Ith_Statistics(tab, q+1, k, i)

def SumBetween(T, From, to):
    n = len(T)
    Ith_Statistics(T, 0, n-1, From)
    Ith_Statistics(T, From+1, n-1, to)
    print(T)
    suma = 0
    for i in range(From, to+1):
        suma += T[i]
    return suma


tab = [2, 3, 1, 0, 5, 2, 3, 2]
print(SumBetween(tab, 2, 7))