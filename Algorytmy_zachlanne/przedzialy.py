# Dany jest zbiór punktów X = {x1, . . . , xn} na
# prostej. Proszę podać algorytm, który znajduje minimalną liczbę przedziałów jednostkowych domkniętych,
# potrzebnych do pokrycia wszystkich punktów z X. (Przykład: Jeśli X = {0.25, 0.5, 1.6} to potrzeba dwóch
# przedziałów, np. [0.2, 1.2] oraz [1.4, 2.4]).

def przedzialy(tab):
    n = len(tab)
    tab.sort()
    licz = 1  # ilosc przedzialow
    i = 1  # rozpatrywany punkt - indeks
    pocz = tab[0]  # pocz przedzialu; koniec = pocz + 1
    result = [0]
    result[0] = (pocz, pocz+1)
    for i in range(1,n):
        if tab[i] > pocz + 1:  # tworzymy kolejny przedzial
            licz += 1
            pocz = tab[i]
            result.append((pocz, pocz+1))
    return licz, result


A = [0.25, 0.5, 1.6]
print(przedzialy(A))
