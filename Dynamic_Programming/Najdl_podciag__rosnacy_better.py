def BinarySearch(tab, n, el):
    l = 1
    r = n-1
    maks_ind = 0
    maks = 0
    while l<= r:
        sr = (l+r)//2
        if tab[sr][0] == el:
            return sr
        elif tab[sr][0] < el:
            if tab[sr][0] > maks:
                maks = tab[sr][0]
                maks_ind = sr
            l = sr + 1
        else:
            r = sr - 1
    return maks_ind


def LIS(tab):
    n = len(tab)
    res = [[] for i in range(n+1)]
    res[1].append(tab[0])
    size = 2
    for i in range(1, n):
        ind = BinarySearch(res, size, tab[i])
        if ind == 0:
            ind = 1
        else:
            if ind == size - 1:
                size += 1
                ind += 1
        res[ind].append(tab[i])
        if res[ind][0] > tab[i]:
            res[ind][0], res[ind][len(res[ind])-1] = res[ind][len(res[ind])-1], res[ind][0]
    print(res)
    i = n-1
    while res[i] == []:
        i -= 1
    return i


A = [3,1,5,7,2,4,9,3,17,3]
B = [2, 3, 1, 5, 7, 6, 8, 9, 1]
print(LIS(A))