def przyczepa(W,K):
    n = len(W)
    W.sort(reverse = True)
    print(W)
    masa = K #tyle ile moge jeszcze uzbierac
    i = 0 #rozpatrywany przedmiot
    result = []
    while i<n and masa <=K:
        if W[i] <= masa: #biore
            masa -= W[i]
            result.append(i)
        i += 1
    return result


A = [2, 2, 4, 8, 1, 8, 16]
maks = 27
print(przyczepa(A,maks))