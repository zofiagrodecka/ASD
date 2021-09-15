#ostatnie wystapienie "zazwyczaj"
def BinarySearch(tab, el):
    l = 0
    r = len(tab)-1
    while l<= r:
        sr = (l+r)//2
        if el == tab[sr]:
            return sr
        elif el > tab[sr]:
            l = sr+1
        else:
            r = sr-1
    return -1

# lepszy ?
def BinarySearch2(tab, p, k, el):
    if p <= k:
        sr = p + (k-p)//2
        if el == tab[sr]:
            return sr
        elif el < tab[sr]:
            return BinarySearch2(tab, p, sr-1, el)
        else:
            return BinarySearch2(tab, sr+1, k, el)
    return -1  # jak dasz tu p to zwróci indeks, gdzie powinna być szukana wartość


tab = [1, 2, 4, 5, 5]
print(BinarySearch2(tab, 0, 4, 6))