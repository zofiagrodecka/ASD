#  Given a rod of length n inches and a table of prices pi for i D 1; 2; : : : ; n,
#  determine the maximum revenue rn obtainable by cutting up the rod and selling the pieces.
#  Note that if the price pn for a rod of length n is large enough, an optimal solution may require no cutting at all.

#  f(i) = max dochod z ucinania i sprzedazy kija dlugosci i
#  f(i) = max po m, gdzie 1 <= m <= i z (price[m] + f(i-m))

def rod_cutting(P):
    n = len(P)
    F = [0]*(n+1)
    parent = [0]*(n+1)
    for i in range(1, n+1):
        for m in range(1, i+1):
            if F[i] < P[m-1] + F[i-m]:
                F[i] = P[m-1] + F[i-m]
                parent[i] = m
    print(F)
    print(parent)
    i = n
    res = []
    while parent[i] != i:
        res.append(parent[i])
        i = i-parent[i]
    res.append(i)
    return F[n], res


price = [1,5,8,9,10,17,17,20,24,30]
print(rod_cutting(price))