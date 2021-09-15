import math


class node:
    def __init__(self):
        self.sum = 0
        self.range = [-1]*2


def constructST(tab, p, k, tree, index):
    if p == k:
        tree[index] = tab[p]
        return tab[p]
    mid = p + (k - p) // 2
    tree[index] = constructST(tab, p, mid, tree, index * 2 + 1) + constructST(tab, mid + 1, p, k, index * 2 + 2)
    return tree[index]


def segment_Tree(tab, n):
    height = (int)(math.ceil(math.log2(n)))
    max_size = 2 * (int)(2 ** height) - 1
    tree = [0] * max_size
    constructST(tab, 0, n - 1, tree, 0)
    return tree

class IntervalSums:
    def __init__(self, n):  # tworzy tablcę rozmiaru n, zainicjowaną zerami
        tab = [0]*n
        tree = segment_Tree(tab, n)

    #def set( self, i, val ):  # zmienia zawartosc tablicy pod indeksem i na val

    #def interval( self, i, j ):  # zwraca sumę elementów tablice na pozycjach od i do j wlacznie




"""Przykładowe użycie klasy:"""
IS = IntervalSums(4) # tworzy tablicę [0,0,0,0]
print(IS.tab)
"""IS.set(0,10) # [10,0,0,0]
IS.set(2,-2) # [10,0,-2,0]
IS.set(3,1) # [10,0,-2,1]
IS.interval(0,3) # zwraca 10+0+(-2)+1 = 9
IS.interval(1,2) # zwraca 0-2 = -2"""
