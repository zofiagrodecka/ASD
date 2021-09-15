# Dany jest cięg macierzy A1, A2, . . . , An. Ktoś chce policzyć iloczyn
# A1A2 · · · An. Macierze nie sa koniecznie kwadratowe (ale oczywiście znamy ich rozmiary).
# Zależnie w jakiej kolejnosci wykonujemy mnożenia, koszt obliczeniowy moze byc różny—należy podać algorytm znajdujący
# koszt mnożenia przy optymalnym doborze kolejności.

def macierze(tab):
    n = len(tab)
    F = [None]*n
    for i in range(n):
        F[i] = [0]*n
    n_wierszy = n-1
    for i in range(1, n):
        for w in range(0, n_wierszy):
            k = i + w
            for m in range(w, k):
                if F[w][k] == 0 or (F[w][m] + F[m+1][k] + (tab[w][0]*tab[m][1]*tab[k][1])) < F[w][k]:
                    F[w][k] = F[w][m] + F[m+1][k] + (tab[w][0]*tab[m][1]*tab[k][1])
        n_wierszy -= 1
    for i in range(n):
        for j in range(n):
            print(F[i][j], end=' ')
        print()
    return F[0][n-1]


T = [(2,20), (20, 1), (1, 10), (10, 5)]
print(macierze(T))