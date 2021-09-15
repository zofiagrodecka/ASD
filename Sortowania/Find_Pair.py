def Merge(tab, p, sr, k):
    T = [0]*(k+1)
    l = p
    r = sr+1
    i = p
    while l <= sr and r <= k:
        if tab[l] < tab[r]:
            T[i] = tab[l]
            l += 1
        else:
            T[i] = tab[r]
            r += 1
        i+=1
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


def MergeSort(tab, p, k):
    if p != k:
        sr = (p+k)//2
        MergeSort(tab, p, sr)
        MergeSort(tab, sr+1, k)
        Merge(tab, p, sr, k)
    return

def find_pair(tab, sum):
    l = 0
    r = len(tab)-1
    MergeSort(tab, l, r)
    while(l<r):
        if tab[l] + tab[r] == sum:
            return True
        elif tab[l] + tab[r] < sum:
            l += 1
        else:
            r -= 1
    return False


A = [100, 200, 96, 54, 32, 11]
if find_pair(A,300):
    print("YES")
else:
    print("NO")