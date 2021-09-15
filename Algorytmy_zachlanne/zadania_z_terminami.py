# Mamy dany zbiór zadań T = {t1, . . . , tn}.
# Każde zadanie ti dodatkowo posiada:
# (a) termin wykonania d(ti) (liczba naturalna) oraz
# (b) zysk g(ti) za wykonanie w terminie (liczba naturalna).
# Wykonanie każdego zadania trwa jednostkę czasu. Jeśli zadanie ti zostanie wykonane
# przed przekroczeniem swojego terminu d(ti), to dostajemy za nie nagrodę g(ti) (pierwsze wybrane zadanie
# jest wykonywane w chwili 0, drugie wybrane zadanie w chwili 1, trzecie w chwili 2, itd.).
# Proszę podać algorytm, który znajduje podzbiór zadań, które można wykonać w terminie i który prowadzi
# do maksymalnego zysku. Proszę uzasadnić poprawność algorytmu

"""
DOWOD:
A - rozwiazanie optymalne
x - zajecie konczace sie najwczesniej ze wszystkich, jezeli sa inne zajecia konczace sie tak samo wczesnie, to maja one mniejszy zysk niz x
a - zajecie konczace sie najwczesniej z zajec nalezacych do A

1. jezeli x == a => nie jesteśmy pozbawieni szansy znalezienia rozwiązania optymalnego, bo je wybralismy do naszego rozwiązania
2. W przeciwnym przypadku:
Wtedy a:
 I konczy sie pozniej niz zajęcie x => gdy dodamy zajecie x do naszego zbioru A => otrzymamy jeszcze lepsze rozwiazanie <--- SPRZECZNE
 II konczy sie w tym samym czasie, ale ma mniejszy zysk niz g(x) => możemy zamienić zajęcie a z zajęciem x, nie zepsuje nam to rozwiazania =>  otrzymamy jeszcze lepsze rozwiazanie <--- SPRZECZNE
Wniosek:
wybierajac zajecie ktore sie konczy najwczesniej na pewno nie pozbawiamy sie szansy znalezienia rozwiazania optymalnego
+ WŁASNOŚĆ OPTYMALNEJ PODSTRUKTURY:
Rozwiazujac pierwszy podproblem dostajemy nastepny, tego samwgo typu, problem, ktory nalezy rozwiazac w sposob optymalny
"""

def fun(x):
    return x[0]

def deadlines(tab): #tab = [(termin, zysk), ...]
    tab.sort(key=fun)
    print(tab)
    n = len(tab)
    current = 0  # indeks rozpatrywanego zadania, ktore wybralismy
    time = 0  # chwila, w ktorej wykonuje zadanie current
    profit = 0  # aktualny zysk
    chores = []
    while current < n:
        i = current+1
        max_profit = tab[current][1]
        ind_max = current
        # szukam max zysku jezeli kilka zadan sie konczy w tym samym czasie,
        # ewentualnie sprawdzam, jak daleko trzeba przeskoczyć, jezeli juz sie spoznilismy z ich wykonaniem
        while i < n and tab[i][0] == tab[current][0]:
            if max_profit < tab[i][1]:
                max_profit = tab[i][1]
                ind_max = i  # indeks zadania z najwiekszym profitem
            i += 1
        if tab[current][0] >= time:  # zajecie current miesci sie w deadlinie
            chores.append(tab[ind_max])
            time += 1
            profit += max_profit
        current = i  # przeskakujemy do zadan z wiekszym deadlinem
    return profit, chores


A = [(7,1), (3,5), (5,5), (2,1), (4,3), (7,10), (2,2), (3,8)]
print(deadlines(A))