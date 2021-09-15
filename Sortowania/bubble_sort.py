def bubble_sort(tab):
    n = len(tab)
    for i in range(0,n-1): #ile kubelkow
        for j in range(0, n-i-1): #zamiana
            if tab[j] > tab[j+1]:
                tab[j], tab[j+1] = tab[j+1], tab[j]

#zal: mam tylko 5 elementow w tablicy w zlym miejscu
def sort(tab):
    n = len(tab)
    for i in range(0, 5):
        for j in range(0, n-i-1):
            if tab[j] > tab[j+1]:
                tab[j], tab[j+1] = tab[j+1], tab[j]
    return tab

arr = [1, 20, 6, 5, 12, 8, 2]
print(sort(arr))
bubble_sort(arr)
print(arr)