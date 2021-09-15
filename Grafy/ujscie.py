#O(n)
#REPREZENTACJA MACIERZOWA!!!
"""
UJSCIE - wierzcholek w grafie skierowanym. Z kazdego innego wierzcholka istnieje krawedz do ujscia oraz z ujscia nie istnieje krawedz do zadnego wierzcholka
"""
def sink(G):
    n = len(G)
    i = 0
    j = 0
    while j < n and j < n:
        if G[i][j] == 0:
            j += 1
        else:
            i += 1
    if i >= n:
        return None
    if j >= n:
        for k in range(n):
            if G[i][k] == 1:
                return None
        j = i
        for k in range(i+1, n):
            if G[k][j] == 0:
                return None
        return j


G = [[0 for i in range(6)] for j in range(6)]
for i in range(6):
    G[i][4] = 1
for i in range(6):
    G[4][i] = 0
G[1][0] = 1
G[1][2] = 1
G[3][0] = 1
G[5][0] = 1
G[5][4] = 1
print(sink(G))