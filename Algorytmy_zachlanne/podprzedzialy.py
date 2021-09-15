def begin(A):
    return A[0]


def length(A):
    return A[1] - A[0]


def nadzbior(A,B):  # czy A jest nadzbiorem B
    if A[0] <= B[0] and A[1] >= B[1]:
        return True
    return False


def podprzedzialy(tab):
    n = len(tab)
    tab.sort(key=begin)
    tab.sort(key=length, reverse=True)
    print("sorted: ", tab)
    res = []
    for i in range(n-1):
        j = i+1
        while j < n-1 and not nadzbior(tab[i], tab[j]):
            j += 1
        if nadzbior(tab[i], tab[j]):
            res.append(tab[i])
    return res


T = [(3, 9), (1,2), (5,7), (3,8), (5,7)]
I=[(1,2),(3,5),(2,4),(8,9),(2,4),(1,5),(5,7),(2,7)]
print(podprzedzialy(T))
print(podprzedzialy(I))