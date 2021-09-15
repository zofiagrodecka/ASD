# Dana jest n elementowa tablica A = [(b1, e1), . . . ,(bn, en)], gdzie każda para (bi, ei) oznacza zajęcia
# rozpoczynające się w chwili bi i kończące w chwili ei.
# Proszę zaimplementować funkcję tasks(A), która zwraca ile maksymalnie zajęć
# można wybrać tak, by na siebie nie nachodziły. Można założyć, że wszystkie
# liczby w tablicy A są naturalne. Przedziały należy traktować jako otwarte, czyli
# np. zajęcia (1, 3) oraz (3, 5) nie nachodzą na siebie

# Dowod:
"""
TEZA: Wybieranie przedziału kończącego się najwcześniej prowadzi do rozw optymalnego (nie pozbawia nas szansy na rozwiązanie problemu)
Ponieważ, gdy już go wybierzemy i "rozwiążemy 1 podproblem", to zostajemy z takim samym podproblemem
Niech:
A - najliczniejszy zbiór przedziałów, które na siebie nie nachodzą (rozwiazanie optymalne)
a - zajecie, ktore konczy sie najwczesniej ze wszystkich zajęć
b - zajecie, ktore konczy sie najwczesniej z zajec nalezacych do A

1. Jeżeli a należy do A => nie jesteśmy pozbawieni szansy znalezienia rozwiązania optymalnego, bo je wybralismy do naszego rozwiązania
2. W przeciwnym przypadku:
Mamy w naszym rozwiązaniu A zajęcie b.
Z definicji musi ono się kończyć później niż a, ale wcześniej niż wszystkie inne zajęcia z rozwiązania A
zatem:
jesli z rozwiązania optymalnego skreslimy zadanie b, to mozemy do niego dolozyc nasze zajecie a, poniewaz ono nie moglo kolidować z żadnym innym przedzialem z rozwiązania optymalnego, za wyjatkiem tego b, ktore usunelismy.
Wniosek:
wybierajac przedzial ktory sie konczy najwczesniej na pewno nie pozbawiamy sie szansy znalezienia rozwiazania optymalnego poniewz ta 1 decyzja ktora podejmujemy nie prowadzi do żadnych problemow
Dodatkowo: rozwiazujac pierwszy podproblem dostajemy nastepny, tego samwgo typu, podproblem, ktory nalezy ozwiazac w sposob optymalny <--- WŁASNOŚĆ OPTYMALNEJ PODSTRUKTURY
"""

def end(val): #funkcja zwracajaca 2-gi element z krotki, ktora jest jej argumentem
    return val[1]


def tasks(A):
    n = len(A)
    licz = 1 #licz liczy ilosc wybranych zajec
    zaj = 0 #indeks ostatniego zajecia, ktore wybralismy
    nast = 1 #indeks zajecia, ktore konczy sie pozniej niz zaj, ale przed cala reszta, ktora musimy jeszcze rozwazyc czy wybrac
            #bedziemy sprawdzac czy bierzemy nast do naszego planu(rozwiazania)

    A.sort(key=end) #sortuje tablice A wzgledem czasu zakonczenia zajec

    while(nast < n): #sprawdzamy wszystkie mozliwe zajecia zaczynajac od 1, bo 0 juz wybralismy
        if A[nast][0] >= A[zaj][1]: #jezeli zajecie ktore teraz rozwazamy nie koliduje z ostatnim wybranym to je dodajemy do rozwiazania
            zaj = nast
            licz += 1
            nast = zaj + 1
        else: #jezeli rozwazane zajecie koliduje z ostatnim wybranym, to rozwazamy kolejne, ktore sie konczy pozniej niz ostatnie rozwazane, ale wczesniej niz reszta do rozwazenia
            nast += 1
    return (licz) #zwracamy ilosc zajec wybranych


# elementarny test, powinien wypisać 2
print(tasks([ (0,10), (10,20), (5,15) ]))