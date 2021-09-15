def BinarySearch_left_boundary(tab,el):
    l = 0
    r = len(tab)-1
    while l <= r:
        sr = (l+r)//2
        if el > tab[sr]:
            l = sr+1
        else:
            r = sr-1
    return l

def BinarySearch_right_boundary(tab, el):
    l = 0
    r = len(tab)-1
    while l <= r:
        sr = (l+r)//2
        if el >= tab[sr]:
            l = sr+1
        else:
            r = sr-1
    return r

def CountOcurrences(tab, el):
    return (BinarySearch_right_boundary(tab,el) - BinarySearch_left_boundary(tab,el) + 1)


tab = [1, 2, 2, 2, 2, 2, 3, 4, 5, 5, 5]
print(CountOcurrences(tab,2))