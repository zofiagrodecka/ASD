def Knapsack(W,P,MaxW):
    n = len(W)
    F = [None]*n
    for i in range(n):
        F[i] = [0]*(MaxW+1)
    for w in range(W[0], MaxW+1):
        F[0][w] = P[0]
    for i in range(1,n):
        for w in range(1, MaxW+1):
            F[i][w] = F[i-1][w]
            if w >= W[i]:
                F[i][w] = max(F[i-1][w], F[i-1][w-W[i]]+P[i])
    #wypisywanie wyniku
    r = F[n-1][MaxW]
    w = MaxW
    result = []
    for i in range(n-1, 0, -1):
        if F[i-1][w] != r:
            result.append(i)
            r = r - P[i]
            w = w - W[i]
    if r > 0:
        result.append(0)

    return (F[n-1][MaxW], result)


W = [4, 1, 2, 4, 3, 5, 10, 3]
P = [7, 3, 2, 10, 4, 1, 7, 2]
MaxW = 10
print(Knapsack(W, P, MaxW))