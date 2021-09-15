# Dana jest n elementowa tablica A = [(P1, W1), . . . ,(Pn, Wn)] opisująca egzemplarz ciągłego problemu plecakowego;
# A opisuje dostępne płyny a k objętość plecaka (a raczej pojemnika; k jest podane w litrach).
# Dla i-go przedmiotu Pi oznacza jego wartość za wszystkie dostępne Wi litrów.
# Proszę zaimplementować funkcję knapsack(A,k), która oblicza wartość najlepszego pojemnika, jaki można uzyskać.

# Dowod:
"""
A - rozwiazanie, ktore znajduje nasz algorytm
A zawiera pewnien wynik: a(1) >= a(2) >= a3 >= ... , gdzie:
a(i) - część przedmiotu i, którą wybraliśmy do rozwiązania A
B - rozwiązanie optymalne
a(1) = maksymalna ilość przedmiotu 1 (bo tak dziala nasz algorytm) => W B nie może być większej ilości przemdiotu 1 niż jest w A
Jeżeli b(1) < a(1) = w B jest mniejsza ilość 1 przedmiotu niż w A
Zauważamy:
Na poziomie b(1) mamy wziętą taką samą ilość przedmiotu 1.
Natomiast powyżej: wiemy, że w zakresie od końca b(1) (z B) do końca a(1) (z A) rozwiązanie A uzyskało lepszy wynik, ponieważ tą samą pojemność wypełniło bardziej opłacalnymi przedmiotami (wieksza czescia a(1))
Zatem możemy zastąpić tą część od b(1) do a(1) fragmentem z rozwiązania A na tej samej pojemności
Ponieważ to bylo lepsze rozwiazanie oraz nie uzywamy nigdzie wiekszej ilosci a(1):
Zatem:
z założenia ze nasze rozw optymalne nie wykorzystalo w calosci najbardziej optymalnego przedmiotu => sprzecznosc (bo dalo sie znalezc rozwiazanie jeszcze lepsze niz optymalne)
Wnioski:
Zaczynając od wybierania do rozwiązania maksymalnej ilości przedmiotu najbardziej opłacalnego, nie popełniamy błędu
+ WŁASNOŚĆ OPTYMALNEJ PODSTRUKTURY:
Jak wypełniamy plecak do pojemności, którą zużywa pierwszy najbardziej opłacalny przedmiot to dostajemy podproblem tego samego typu ktory nalezy rozwiazac optymalnie zeby uzyskac optymalne rozwiazanie
"""

def oplacalnosc(val): #funkcja zwracajaca oplacalnosc wziecia przedmiotu(krotki), ktory jest jej argumentem
    return val[0]/val[1]


def knapsack(A,k):
    n = len(A)
    A.sort(reverse=True, key=oplacalnosc) #sortuje tablice(pojemnik) nierosnaco wzgledem oplacalnosci zabrania przedmiotow(plynow)
    i = 0 #indeks przedmiotu(plynu), ktory teraz chce wziac
    waga = 0 #waga, ktora juz uzbieralam w pojemniku
    profit = 0 #zysk ktory juz mam z wzietych przedmiotow(plynow)

    # sprawdzam wszystkie dostepne przedmioty i zabieram jak najwiecej sie da zaczynajac od najbardziej oplacalnych
    #jak uzbieram wage k albo dojde do konca tablicy z dostepnymi przedmiotami(plynami), to koncze zbierac
    while(waga < k and i < n):
        if A[i][1] <= (k - waga): #biore caly i-ty przedmiot(plyn), jezeli cala jego waga nie przekracza wartosci masy, ktora moge jeszcze uzbierac
            waga += A[i][1]
            profit += A[i][0]
        else: #biore tyle ile moge i-tego przedmiotu(plynu), by nie przekroczyc maksymalnej wagi k
            profit += (A[i][0]*(k-waga))/A[i][1] #zysk z wziecia (k-waga) litrow przedmiotu(plynu)
            waga += (k-waga)
        i+=1
    return (profit)


# elementarny test, powinien wypisać 12
print( knapsack([ (1,1), (10,2), (6,3) ], 3))