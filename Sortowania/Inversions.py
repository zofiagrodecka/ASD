def MergeCount(tab, p, sr, k, res):
    T = [0]*(k+1)
    l = p
    r = sr + 1
    i = p
    while l<=sr and r<=k:
        if tab[l] > tab[r]:
            res += (sr-l+1)
            T[i] = tab[r]
            r += 1
        else:
            T[i] = tab[l]
            l += 1
        i += 1

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
    return res



def CountInversions(tab, p, k, res): #(tab, 0, len(tab)-1, 0)
    if p < k:
        middle = (p+k)//2
        res += CountInversions(tab, p, middle, res) + CountInversions(tab, middle+1, k, res) + MergeCount(tab, p, middle, k, res)
    return res


tab = [1, 5, 4, 6, 5]
T = [1, 20, 6, 4, 5]
print(CountInversions(T, 0, len(tab)-1, 0))