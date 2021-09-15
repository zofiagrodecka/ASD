# f(i,d) = maksymalna dlugosc samochodow jaka moze wjechać na 1 pas o dlugosci d spośród aut o indeksach od 0 do i
#
# f(i,d) = max( f(i-1, d), f(i-1, d - tab[i]) + tab[i])
#            { 0, tab[0] > d
# f(0, d) = {
#            { tab[0], tab[0] <= d
#
# f(i, 0) = 0

def max_lane_length(tab, D):
    n = len(tab)
    F = [0] * n
    for i in range(n):
        F[i] = [0]*(D+1)
    if tab[0] <= D:
        for d in range(tab[0], D+1):
            F[0][d] = tab[0]

    for i in range(1, n):
        for d in range(1, D+1):
            F[i][d] = F[i-1][d]
            if d - tab[i] >= 0 and F[i-1][d - tab[i]] + tab[i] > F[i][d]:
                    F[i][d] = F[i-1][d - tab[i]] + tab[i]

    for i in range(n):
        for j in range(D+1):
            print(F[i][j], end=' ')
        print()
    return F


def ferry(tab, D):
    n = len(tab)
    F = max_lane_length(tab, D)
    lane1 = []
    i = n-1
    d = D
    while F[i][d] > 0 and i >= 0 and d >= 0:
        if F[i-1][d] != F[i][d]:
            lane1.append(i)
            d = d - tab[i]
        i -= 1
    if F[i][d] > 0:
        lane1.append(i+1)
    s = 0
    j = len(lane1) - 1
    i = 0
    lane2 = []
    while i < n or j >= 0:
        if lane1[j] != i:
            if s + tab[i] <= D:
                s += tab[i]
                lane2.append(i)
            else:
                if lane1[j] > i:
                    lane1 = lane1[j+1:]
                break
        else:
            j -= 1
        i += 1

    return lane1, lane2


tab = [1,2,3,8,4]
tab2 = [5,1,2,8,2]
A=[1,2,3,4,2,4,5]
B = [4, 9, 2, 3, 2, 1]
test = [5, 6, 5, 9]
print(ferry(A, 10))