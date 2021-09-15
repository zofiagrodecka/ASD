# Dana jest szachownica A o wymiarach n × n. Szachownica
# zawiera liczby wymierne. Należy przejść z pola (1, 1) na pole (n, n) korzystając jedynie z ruchów “w dół”
# oraz “w prawo”. Wejście na dane pole kosztuje tyle, co znajdująca się tam liczba. Proszę podać algorytm
# znajdujący trasę o minimalnym koszcie

def szachownica(tab):
    n = len(tab)
    F = [0]*n
    for i in range(n):
        F[i] = [0]*n
    F[0][0] = tab[0][0]
    for j in range(1,n):
        F[0][j] = F[0][j-1] + tab[0][j]
    for i in range(1,n):
        F[i][0] = F[i-1][0] + tab[i][0]
    for i in range(1,n):
        for j in range(1,n):
            F[i][j] = min(F[i-1][j], F[i][j-1]) + tab[i][j]
    for i in range(n):
        for j in range(n):
            print(F[i][j], end=" ")
        print(" ")


A = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
szachownica(A)
