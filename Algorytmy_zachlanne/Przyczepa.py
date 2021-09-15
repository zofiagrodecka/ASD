# Mamy przyczepę o pojemności K kilogramów oraz zbiór ładunków o
# wagach w1, . . . , wn. Waga każdego z ładunków jest potęgą dwójki (czyli, na przykład, dla siedmiu ładunków
# wagi mogą wynosić 2, 2, 4, 8, 1, 8, 16, a pojemność przyczepy K = 27). Proszę podać algorytm zachłanny (i
# uzasadnić jego poprawność), który wybiera ładunki tak, że przyczepa jest możliwie maksymalnie zapełniona
# (ale bez przekraczania pojemności) i jednocześnie użyliśmy możliwie jak najmniej ładunków. (Ale jeśli da się
# np. załadować przyczepę do pełna uzywając 100 ładunków, albo zaladować do pojemności K − 1 używając
# jednego ładunku, to lepsze jest to pierwsze rozwiązanie)

def przyczepa(tab, K):
    n = len(tab)
    tab.sort(reverse=True)
    current = 0
    miejsce = K  # aktualne miejsce w przyczepie
    wagi = []
    while current < n:
        if tab[current] <= miejsce:
            miejsce -= tab[current]
            wagi.append(tab[current])
        current += 1
    return wagi, miejsce


A = [4, 8, 1, 8, 16]
print(przyczepa(A,30))