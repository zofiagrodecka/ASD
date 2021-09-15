# Mamy daną tablicę z nominałami monet stosowanych w pewnym dziwnym kraju, oraz kwotę T.
# Proszę podać algorytm, który oblicza minimalną ilość monet potrzebną do wydania
# kwoty T (algorytm zachłanny, wydający najpierw największą monetę, nie działa: dla monet 1, 5, 8 wyda
# kwotę 15 jako 8 + 5 + 1 + 1 zamiast 5 + 5 + 5)

"""
f(i) = minimalna liczba monet do wydania kwoty i
f(i) = 1 + min( f(i-tab[j]) | j < n and i >= tab[j] )
f(0) = 0
"""

def MLM(tab, T):
    n = len(tab)
    F = [10000] * (T+1)
    F[0] = 0
    P = [None]*(T+1)
    for i in range(T+1):
        for j in range(n):
            if i >= tab[j] and F[i-tab[j]] < F[i]:
                F[i] = F[i-tab[j]] + 1
                P[i] = tab[j]

    res = []
    last = T
    while P[last] != None:
        res.append(P[last])
        last -= P[last]
    return F[T], res


A = [1, 5, 8]
print(MLM(A,13))