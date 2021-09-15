def parent(i):
    return i//2
def left(i):
    return i*2
def right(i):
    return 2*i + 1

def heapify(k, i):
    l = left(i)
    r = right(i)
    maks = i
    size = k[0]
    if l <= size and k[l] > k[maks]:
        maks = l
    if r <= size and k[r] > k[maks]:
        maks = r
    if maks != i:
        k[i], k[maks] = k[maks], k[i]
        heapify(k, maks)


def BuildHeap(k):
    for i in range(k[0]//2, 0, -1):
        heapify(k, i)


def HeapSort(k):
    size = k[0]
    BuildHeap(k)
    for i in range(size, 1, -1):
        k[i], k[1] = k[1], k[i]
        k[0] -= 1
        heapify(k, 1)


tab = [9, 5, 8, 1, 12, 9, 10, 9, 4, 2]
tab[0] == len(tab)
HeapSort(tab)
print(tab)