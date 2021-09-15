def CountingSort(A, cyfra):
    n=len(A)
    k = n-1
    n = len(A)
    B = [0]*n
    C = [0]*(k+1)
    for i in range(n):
        liczba = A[i]//cyfra
        r = liczba % n
        C[r] += 1
    for i in range(1,k+1):
        C[i] += C[i-1]
    for i in range(n-1, -1, -1):
        liczba = A[i] // cyfra
        r = liczba % n
        C[r] -= 1
        B[C[r]] = A[i]
    for i in range(n):
        A[i] = B[i]


def radix_sort(tab):
    maks = max(tab)  # szukam maksymalnej liczby zeby znac maksymalna dlugosc liczb
    n = len(tab)
    cyfra = 1  # "cyfra" wg ktorej sortuje
    while maks > 1:
        CountingSort(tab, cyfra)
        maks = maks // cyfra
        cyfra *= n


tab = [224, 200, 102, 49, 23, 43, 222, 93, 78, 123, 23, 21, 211, 155, 178]
radix_sort(tab)
print(tab)