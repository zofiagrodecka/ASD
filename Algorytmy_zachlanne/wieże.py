# Grupa m dzieci bawi się w układanie możliwie jak największej wieży. Każde dziecko ma klocki różnej wysokości.
# Pierwsze dziecko ma klocki o wysokościach w1^1, w2^1,...,wn1^1, drugie dziecko klocki o wysokościach
# w1^2,...,wn2^2 itd. Dzieci właśnie poszły zjeść deser zanim ułożą swoje wieże, ale jedno dziecko zostało.
# Ma teraz okazję, żeby podebrać kilka klocków innym dzieciom tak, żeby jego wieża była najwyższa.
# Proszę podać możliwie najszybszy algorytm rozwiązujący ten problem, który zabiera minimalną ilość klocków.
#
# Sortuję rosnąco klocki każdego dziecka, oraz wyliczam sumę wysokości wszystkich  klocków dla każdego dziecka.
# Następnie za każdym razem podchodzę do najwyższej wieży i zabieram największy klocek, układam swoją wieżę dopóki
# nie jest ona wyższa niż wszystkie inne.

def wieza(tab):
    m = len(tab)
    for i in range(m):
        tab[i].sort()
    print(tab)
    sums = [0]*m
    max_sum = 0
    for i in range(m):
        for el in tab[i]:
            sums[i] += el
        if sums[i] > max_sum:
            max_sum = sums[i]
            max_sum_ind = i
    print(sums)
    # Ja jestem dzieckiem z indeksem 0
    res = []
    maks = 0
    ind = -1
    while max_sum != sums[0]:
        maks = 0
        for i in range(m):
            if maks < tab[i][len(tab[i])-1]:
                maks = tab[i][len(tab[i]) - 1]
                ind = i
        res.append((maks, ind))
        tab[ind].pop()
        sums[0] += maks
        sums[ind] -= maks
        if max_sum_ind == ind:
            max_sum = 0
            for i in range(m):
                if sums[i] > max_sum:
                    max_sum = sums[i]
                    max_sum_ind = i
        print(res)
    return res


B=[
    [1,3,5,10,12,7,4],
    [4,49,100,36,16,9,121],
    [64,27,1,125,512],
    [625,1,16]]
print(wieza(B))