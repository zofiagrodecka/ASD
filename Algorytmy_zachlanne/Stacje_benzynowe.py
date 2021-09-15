# Pewien podróżnik chce przebyć trasę z punktu A do punktu  B.
# Niestety jego samochód spala dokładnie jeden litr paliwa na jeden kilometr trasy (można powiedzieć, że
# jedzie czołgiem... znaczenie punktów A i B w ramach obecnej sytuacji geopolitycznej wybierzcie sobie sami).
# W baku mieści się dokładnie D litrów paliwa. Trasa z A do B to prosta, na której znajdują się stacje benzynowe.

# Podpunkt 1: wyznaczyć trasę, na której tankujemy minimalną liczbę razy.
"""
DOWOD:
A - rozwiazanie ktore znajduje nasz algorytm
a(i) - i-ta stacja, na której zatankowaliśmy, wybrana do rozwiązania A
B - rozwiazanie optymalne
b(i) - i-ta stacja na ktorej zatankowalismy, wybrana do rozwiazania B
Zauważamy:
a(1) = najdalsza stacja, do ktorej jestem w stanie dojechac (def algorytmu) => W B b(1) nie moze byc dalej niz a(1)
1.Jeżeli a(1) == b(1) => nie jesteśmy pozbawieni szansy znalezienia rozwiązania optymalnego, bo je wybralismy do naszego rozwiązania
2. W przeciwnym przypadku: b(1) - stacja wczesniej niz a(1)
W takiej sytuacji możemy zastąpić b(1) przez a(1), ponieważ jestesmy w stanie dojechac do a(1) (def) oraz nie zwiększa nam to liczby tankowań, bo nadal mamy 1 tankowanie, zmienilismy tylko stacje
Wniosek:
Wybierając stację, która jest w odleglosci najwiekszej, gdzie tylko mozemy dojechac nie pozbawiamy sie szansy znalezienia rozwiazania optymalnego,
poniewz ta 1 decyzja ktora podejmujemy nie prowadzi do żadnych problemow
+ WŁASNOŚĆ OPTYMALNEJ PODSTRUKTURY:
Rozwiazujac pierwszy podproblem (wybierajac pierwsza stacje) dostajemy nastepny, tego samego typu, podproblem, ktory nalezy rozwiazac w sposob optymalny
"""

def stacje(A, D):
    n = len(A)
    licz_tankowan = 0  # w miescie A tankuje na maxa ale to sie nie wlicza do rozwiazania
    dystans = A[1] # tyle ile juz przejechalam => musze byc w stanie dojechac do 1 stacji, bo inaczej nie ma rozwiazania
    benzyna = D - A[1]  # aktualna ilosc benzyny w baku
    current = 1  # aktualna stacja, do ktorej dojechalismy
    stacje = []
    while dystans < A[n-1]: # dopoki nie dojechalismy do B
        if benzyna - (A[current+1]-A[current]) < 0:  # nie dojedziemy do nastepnej stacji
            # tankujemy tu
            licz_tankowan += 1
            benzyna = D
            stacje.append(current)
        # po tankowaniu lub nie jedziemy do nastepnej stacji
        benzyna = benzyna - (A[current + 1] - A[current])
        current += 1
        dystans = A[current]
    return licz_tankowan, stacje


A = [0, 200, 375, 550, 750, 950]  # liczba to odleglosc do danej stacji od A
#print(stacje(A,400))

# ?? Podpunkt 2: wyznaczyć trasę, której koszt jest minimalny (wówczas znamy jeszcze dla każdej stacji cenę za litr
# paliwa, nie musimy zawsze tankować do pełna).

"""
Na odleglosci D od stacji na ktorej jestem znajduje najtansza stację i tankuję na stacji current tyle żeby dojechać do tej najtańszej.

DOWOD:
A - rozwiazanie, ktore znajduje nasz algorytm
a(1) - pierwsza najtansza stacja na odleglosci D
B - rozwiązanie optymalne
b(1) - pierwsza stacja do ktorej dojade na odleglosci D wybrana do B
Zauważam:
W B nie może być tańszej stacji niż a(1), wybrana do A (def)
1. Jeżeli a(1) == b(1) => nie jesteśmy pozbawieni szansy znalezienia rozwiązania optymalnego, bo je wybralismy do naszego rozwiązania
2. W przeciwnym przypadku: b(1) jest droższa od a(1)
Jeżeli zamienimy b(1) w rozwiazaniu optymalnym z a(1) => uzyskamy jeszcze lepsze rozwiazanie,
bo i a(1) i b(1) musza byc na odleglosci, ktora jestem w stanie przejechac, a tankujac na stacji a(1) zaplacimy mniej niz tankujac na b(1) (def) <--- SPRZECZNOSC (bo dalo sie znalezc rozwiazanie jeszcze lepsze niz optymalne)
Wnioski:
Wybierajac najtańszą stację, do której jesteśmy w stanie dojechać nie pozbawiamy się szansy znalezienia rozwiązania optymalnego
+ WŁASNOŚĆ OPTYMALNEJ PODSTRUKTURY:
Rozwiazujac pierwszy podproblem (wybierajac pierwsza stacje) dostajemy nastepny, tego samego typu, podproblem, ktory nalezy rozwiazac w sposob optymalny
"""

def stacje2(tab, D):
    n = len(tab)
    benzyna = D  # aktualna ilosc w baku
    current = 0  # aktualna stacja na ktorej jestem
    koszt = 0  # ile juz wydalam pieniedzy
    stacje = []
    while current < n-1:
        mini = tab[current+1][1]
        i = current + 1
        ind = current + 1
        while i < n and tab[i][0] - tab[current][0] <= D:
            if tab[i][1] < mini:
                mini = tab[i][1]
                ind = i  # indeks nastepnej stacji
            i += 1
        if benzyna - (tab[ind][0] - tab[current][0]) < 0:  # musze zatankować na current tyle by dojechać do ind
            koszt += ((tab[ind][0] - tab[current][0]) - benzyna)*tab[current][1]
            benzyna = 0
            stacje.append(current)
        else:
            benzyna -= (tab[ind][0] - tab[current][0])
        current = ind
    return stacje, koszt


A = [(0, 0), (200, 4.50), (375, 7.8), (550, 5.2), (750,5.0), (950, 6.0), (1000, 0)]
B = [(0, 0), (10, 5), (12, 2), (15, 4), (18, 4), (20, 1)]
print(stacje2(B,10))
