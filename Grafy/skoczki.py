licz = 0

# for the adjacency list:
# (pl.) dla listy sasiedztwa:

def DFSVisit(T, i, j, visited):
    n = len(T)
    global licz
    visited[i][j] = True
    licz += 1
    if 0 <= i - 1 < n and 0 <= j - 2 < n and T[i - 1][j - 2] == 1 and not visited[i - 1][j - 2]:
        DFSVisit(T, i-1, j-2, visited)
    if 0 <= i - 2 < n and 0 <= j - 1 < n and T[i - 2][j - 1] == 1 and not visited[i - 2][j - 1]:
        DFSVisit(T, i-2, j-1, visited)
    if 0 <= i - 2 < n and 0 <= j + 1 < n and T[i - 2][j + 1] == 1 and not visited[i - 2][j + 1]:
        DFSVisit(T, i-2, j+1, visited)
    if 0 <= i - 1 < n and 0 <= j + 2 < n and T[i - 1][j + 2] == 1 and not visited[i - 1][j + 2]:
        DFSVisit(T, i-1, j+2, visited)
    if 0 <= i + 1 < n and 0 <= j - 2 < n and T[i + 1][j - 2] == 1 and not visited[i + 1][j - 2]:
        DFSVisit(T, i+1, j-2, visited)
    if 0 <= i + 2 < n and 0 <= j - 1 < n and T[i + 2][j - 1] == 1 and not visited[i + 2][j - 1]:
        DFSVisit(T, i+2, j-1, visited)
    if 0 <= i + 2 < n and 0 <= j + 1 < n and T[i + 2][j + 1] == 1 and not visited[i + 2][j + 1]:
        DFSVisit(T, i+2, j+1, visited)
    if 0 <= i + 1 < n and 0 <= j + 2 < n and T[i + 1][j + 2] == 1 and not visited[i + 1][j + 2]:
        DFSVisit(T, i + 1, j + 2, visited)
    print( i, j)


def skoczki(T):
    n = len(T)
    ile = 0
    global licz
    visited = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if T[i][j] == 1:
                ile += 1
                if ile == 1:
                    start_i = i
                    start_j = j
    DFSVisit(T, start_i, start_j, visited)
    if licz == ile:
        return True
    else:
        return False


tab = [[0 for i in range(9)] for j in range(9)]
tab[0][0] = 1
tab[0][4] = 1
tab[1][2] = 1
tab[3][3] = 1
tab[5][4] = 1
tab[6][2] = 1
tab[6][6] = 1
tab[4][1] = 1
tab[8][1] = 1
tab[8][7] = 1
tab[6][0] = 1
print(skoczki(tab))



