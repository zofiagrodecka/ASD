# Napisz funkcję, któa zwraca prawdę jeśli z liter słów u, v da się ułożyć słowo w
# (nie jest konieczne wykorzystanie wszystkich liter) oraz fałsz w przeciwnym przypadku.

def possible(u, v, w):
    L = [0]*26
    for i in range(len(u)):
        L[ord(u[i]) - 97] += 1
    for i in range(len(v)):
        L[ord(v[i]) - 97] += 1
    for i in range(len(w)):
        if L[ord(w[i]) - 97] > 0:
            L[ord(w[i]) - 97] -= 1
        else:
            return False
    return True


u, v, w = "durnota", "xyz", "dutanoz"
if possible(u,v,w):
    print("Tak")
else:
    print("Nie")