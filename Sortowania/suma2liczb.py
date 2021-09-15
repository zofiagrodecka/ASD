# O(n)

def sum(tab, s):
    n = len(tab)
    i = 0
    j = n-1
    tab.sort()
    while i <= j:
        if tab[i] + tab[j] == s:
            return True
        elif tab[i] + tab[j] < s:
            i += 1
        else:
            j -= 1
    return False


tab = [2, 3, 1, 0, 5]
print(sum(tab, 9))