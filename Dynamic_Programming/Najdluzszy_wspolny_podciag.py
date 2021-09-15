# Mamy dane dwie tablice, A[n] i B[n]. Należy znaleźć długość ich najdłuższego wspólnego podciągu.

"""
f(i,j) = dlugosc najdluzszego wspolnego podciagu od A[0]... A[i] oraz od B[0]...B[j]

            { 1 + f(i-1, j-1), A[i] == B[j]
f(i,j) =   {
            {  max( f(i-1, j) , f(i, j-1)), A[i] != B[j]

            { 1 , A[0] = B[0]
f(0,0) =   {
            { 0, A[0] != B[0]

            { 1, A[k] = B[0] | k <= i
f(i, 0) =  {
            { 0, wpp

            { 1, B[k] = A[0] | k <= i
f(0,j) =   {
            { 0, wpp
"""

def NWP(A,B):
    n = len(A)
    m = len(B)
    F = [0] * n
    for i in range(n):
        F[i] = [0] * m
    if A[0] == B[0]:
        F[0][0] = 1
    for j in range(1, m):
        if A[0] == B[j]:
            F[0][j] = 1
        else:
            F[0][j] = F[0][j-1]
    for i in range(1, n):
        if A[i] == B[0]:
            F[i][0] = 1
        else:
            F[i][0] = F[i-1][0]
    for i in range(1,n):
        for j in range(1,m):
            if A[i] == B[j]:
                F[i][j] = F[i-1][j-1] + 1
            else:
                F[i][j] = max(F[i - 1][j], F[i][j - 1])
    for i in range(n):
        for j in range(m):
            print(F[i][j], end=' ')
        print()
    print()

    res = []
    i = n-1
    j = m-1
    while i >= 0 and j >= 0:
        if i >= 1 and F[i-1][j] == F[i][j]:
            i -= 1
        elif j >= 1 and F[i][j-1] == F[i][j]:
            j -= 1
        else:
            res.append(A[i])
            i -= 1
            j -= 1
    while i > 0:
        if F[i][0] != F[i-1][0]:
            res.append(A[i])
        i -= 1
    while j > 0:
        if F[0][j] != F[0][j-1]:
            res.append(A[0])
        j -= 1
    if A[0] == B[0]:
        res.append(A[0])
    return F[n-1][m-1], res


A = [8, 12, 10, 50, 2, 13]
B = [2, 3, 1, 2, 9, 8, 9, 12, 5]
b = [2, 3, 1, 2, 9, 12]
C = [2, 3, 1, 5, 7, 6, 8, 9]
D = [1, 2, 3, 5, 6, 7, 8, 9]
print(NWP(C, D))