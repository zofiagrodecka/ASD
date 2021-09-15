def anagrams(x, y):
    if len(x) != len(y):
        return False
    L = [0]*26  # tablica licznikow
    n = len(x)
    for i in range(n):
        L[ord(x[i])-97] += 1
    for i in range(n):
        L[ord(y[i]) - 97] -= 1
    for i in range(n):
        if L[ord(x[i]) - 97] != 0:
            return False
    return True


x, y = "durnota", "rotunda"
if anagrams(x,y):
    print("Tak")
else:
    print("Nie")