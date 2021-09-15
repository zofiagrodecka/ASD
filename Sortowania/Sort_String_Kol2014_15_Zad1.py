# Napisz funkcję sortującą tablicę n stringow różnej długości.

def Sort_Length(A, maks):  # sortuje slowa po długości
    n = len(A)
    C = [0] * (maks+1)
    B = [None]*n
    for i in range(n):
        C[len(A[i])] += 1
    for i in range(1, maks+1):
        C[i] += C[i-1]
    for i in range(n-1, -1, -1):
        C[len(A[i])] -= 1
        B[C[len(A[i])]] = A[i]
    for i in range(n):
        A[i] = B[i]
    return C

def Counting_Sort(A, ind):
    k = 26  # maksymalny rozmiar talibcy C (ilosc liter w alfabecie)
    n = len(A)
    B = [0]*n
    C = [0]*(k)
    for i in range(n):
        C[ord(A[i][ind]) - 97] += 1
    for i in range(1, k):
        C[i] += C[i-1]
    for i in range(n-1, -1, -1):
        C[ord(A[i][ind]) - 97] -= 1
        B[C[ord(A[i][ind]) - 97]] = A[i]
    for i in range(n):
        A[i] = B[i]
    return A

def sortString(A):
    # szukam maksymalnej dlugosci słów
    n = len(A)
    maks = 0
    for i in range(n):
        if len(A[i]) > maks:
            maks = len(A[i])
    # sortuje slowa wg dlugosci + zwraca tablice C (ile elemntow o len <= i)
    C = Sort_Length(A, maks)
    print(C)
    print(A)
    for i in range(maks-1, -1, -1):  # sortuje po i-tej pozycji
        pocz = C[i+1]  # indeks poczatkowy wyrazow o dlugosci i
        A[pocz:] = Counting_Sort(A[pocz:], i)  # sortuje tylko wyrazy o dlugosci >= i-tej
    return A


tab = ["ala", "ma", "kota", "a", "kot", "ma", "ale", "ala", "aaaa", "ab"]
print(sortString(tab))
