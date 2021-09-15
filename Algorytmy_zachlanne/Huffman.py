# Dana jest tablica n liczb naturalnych A. Liczba A[i] mówi ile razy i-ty symbol
# pojawia się w tekście. Proszę zaimplementować funkcję huffman len(A), która oblicza ile bitów zajęłoby
# zapisanie tekstu składającego się właśnie z takiej liczby symboli, jeśli użytoby optymalnego kodu Huffmana.
# Funkcja powinna działać w czasie O(n log n). Podpowiedź: Może się przydać struktura kopca.

#tworze sobie kopiec(tablice) typu min, w ktorym pod indeksem 0 znajduje sie liczba elementow w kopcu, a pod nastepnymi indeksami zawartosc kopca
def parent(i): #indeks roota i-tego elementu w kopcu
    return i//2

def left(i): #indeks lewego syna i-tego elementu
    return i*2


def right(i): #indeks prawego syna i-tego elementu
    return 2*i + 1


def heapify(k,i): #funkcja przywracajaca wlasnosc kopca min
    l = left(i)
    r = right(i)
    mini = i
    size = k[0]
    if l <= size and k[l] < k[mini]:
        mini = l
    if r <= size and k[r] < k[mini]:
        mini = r
    if mini != i:
        k[i], k[mini] = k[mini], k[i]
        heapify(k,mini)


def BuildHeap(k): #funkcja budujaca kopiec min
    size = k[0]
    for i in range(size//2, 0, -1):
        heapify(k,i)


def getmin(k): #funkcja usuwajaca roota kopca oraz zwracajaca jego wartosc
    size = k[0]
    if size != 0:
        result = k[1]
        k[1] = k[size]
        k[0] -= 1
        del k[size]
        heapify(k,1)
        return (result)


def insert(k,x): #funkcja dodajaca do kopca element
    k[0] += 1
    size = k[0]
    k.append(x)
    i = size
    while i>1 and k[i] < k[parent(i)]:
        k[i], k[parent(i)] = k[parent(i)], k[i]
        i = parent(i)


def huffman_len(A):
    B = [0]*1 #tworze tablice, ktora bedzie moim kopcem
    B[0] = len(A) #ustawiam wartosc rozmiaru mojego kopca pod indeksem 0
    B.extend(A) #dodaje do kopca wartosci z tablicy A
    BuildHeap(B) #buduje kopiec min

    #na samym koncu w moim kopcu zostanie tylko 1 element => rozmiar kopca bedzie wynosic 1
    while(B[0] > 1):
        min1 = getmin(B)
        min2 = getmin(B) #wycigam z kopca 2 najmniejsze elementy
        insert(B,min1+min2) #wstawiam do kopca sume 2 najmniejszych elementow, ktore byly w nim uprzednio
        #powtarzam to, dopoki rozmiar kopca bedzie rowny 1, poniewaz wtedy zostanie na kopcu tylko liczba (root) ktorej wartosc bedzie rowna liczbie bitow potrzebnych do zakodowania tego ciagu znakow
    return B[1]


# elementarny test, powinien wypisać 2600
print( huffman_len([200, 700, 180, 120, 70, 30]))

# wydaje mi sie ze ten test powinien wypisac 1300, taki przyklad byl na ostatnim wykladzie i wtedy wynik byl rowny 1300
# jesli sie myle, przepraszam, moze zle zrozumialam polecenie
