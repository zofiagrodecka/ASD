def Knapsack(W,P,MaxW):
    n = len(W)
    F = [None]*n
    Parent = [0]*n

    for i in range(n):
        Parent[i] = [0]*(MaxW+1)

    for i in range (n):
        F[i] = [0]*(MaxW+1)
    for w in range(W[0], MaxW+1):
        F[0][w] = P[0]

    Parent[0][W[0]] = 1 # !!!!!!!!!!!!!!!!

    for i in range(1,n):
        for w in range(1, MaxW+1):
            F[i][w] = F[i-1][w]
            if w >= W[i]:
                F[i][w] = max(F[i-1][w], (F[i-1][w-W[i]]+P[i]))
                if F[i][w] == F[i-1][w-W[i]]+P[i]:
                    Parent[i][w] = 1
    for i in range(n):
        for j in range(MaxW+1):
            print(Parent[i][j], end=' ')
        print()
    res = []
    weight = MaxW
    for i in range(n-1, -1, -1):
        if Parent[i][weight] == 1:
            res.append(i)
            weight -= W[i]
    return (F[n-1][MaxW], res)


W = [4,1,2,4,3,5,10,3]
P = [10,3,2,7,4,1,7,2]
w = [1, 3, 4, 5]
p = [1, 4, 5, 7]
MaxW=7
print(Knapsack(W,P,MaxW))