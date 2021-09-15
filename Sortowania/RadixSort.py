def CountingSort(A, cyfra):
    k = 9
    n = len(A)
    B = [0]*n
    C = [0]*(k+1)
    for i in range(n):
        liczba = A[i]//cyfra
        r = liczba % 10
        C[r] += 1
    for i in range(1,k+1):
        C[i] += C[i-1]
    for i in range(n-1, -1, -1):
        liczba = A[i] // cyfra
        r = liczba % 10
        C[r] -= 1
        B[C[r]] = A[i]
    for i in range(n):
        A[i] = B[i]


def radix_sort(tab):
    maks = max(tab)  # szukam maksymalnej liczby zeby znac maksymalna dlugosc liczb
    cyfra = 1  # cyfra wg ktorej sortuje (1-jednosci, 10-dziesiatki,...)
    while(maks > 1):
        CountingSort(tab, cyfra)
        maks = maks // cyfra
        cyfra *= 10


arr = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(arr)
print("ARR: " , arr)
