def f(F,i,w):
    if F[i][w] >= 0:
        return F[i][w]
    x = f(F,i-1,w)
    if w >= W[i]:
        y = f(F, i - 1, w - W[i]) + P[i]
        F[i][w] = max(x,y)
    else:
        F[i][w] = x
    return F[i][w]


def Knapsack(W,P,MaxW):
    n = len(W)
    F = [None] * n
    for i in range(n):
        F[i] = [0] * (MaxW + 1)
    for w in range(W[0], MaxW + 1):
        F[0][w] = P[0]
    for i in range(1, n):
        for w in range(1, MaxW + 1):
            return f(F,0,MaxW)