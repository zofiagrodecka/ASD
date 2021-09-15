# Dana jest tablica n liczb A. Proszę podać i zaimplementować
# algorytm, który sprawdza, czy da się wybrać podciąg liczb z A, które sumują się do zadanej wartości T.

"""
f(i,s) = czy da sie wybrac podciag liczb o indeksach od 0 do i o sumie t
WYNIK: f(n-1, T); n-rozmiar tablicy, T-szukana suma

f(i,s) = f(i-1, s) v f(i-1, s-A[i]) dla  i >= 1, s >= A[i]
f(i, 0) = True
            { True, A[0] == s
f(0, s) =  {
            { False, A[0] != s
"""

def suma(A,T):
    n = len(A)
    F = [0] * n
    Parent = [0]*n
    for i in range(n):
        Parent[i] = [0] * (T+1)
    for i in range(n):
        F[i] = [False] * (T+1)
    for i in range(n):
        F[i][0] = True
    for i in range(T+1):
        if A[0] == i:
            F[0][i] = True
            Parent[0][i] = 1  # !!!!!!!!!!!!!!!!
    for i in range(1, n):
        for s in range(1, T+1):
            F[i][s] = F[i-1][s]
            if s >= A[i] and F[i-1][s-A[i]] == True:
                F[i][s] = True
                Parent[i][s] = 1

    for i in range(n):
        for j in range(T+1):
            print(F[i][j], end=' ')
        print()
    for i in range(n):
        for j in range(T+1):
            print(Parent[i][j], end=' ')
        print()
    res = []
    s = T
    for i in range(n-1, -1, -1):
        if Parent[i][s] == 1:
            res.append(i)
            s -= A[i]
    return F[n-1][T], res


tab = [3,1,5,7,2,4,9,3]
t = [1, 3, 5, 7, 9, 2]
S = 10
print(suma(t, S))