def find(tab):
    n = len(tab)
    mini = tab[0]
    maks = tab[0]
    for i in range(1,n):
        if tab[i] > maks:
            maks = tab[i]
        if tab[i] < mini:
            mini = tab[i]
    buckets = [[] for _ in range(n)]  # tworze liste n pustych list
    min_max = [None] * n  # tablica najmniejszych i najwiekszych liczb w kazdym kubełku
    for i in range(n):
        min_max[i] = [None] * 2
    for i in range(len(tab)):
        normalised = (tab[i]-mini)/maks
        buck_ind = int(n*normalised)
        buckets[buck_ind].append(tab[i])
        if min_max[buck_ind][0] == None:
            min_max[buck_ind][0] = tab[i]
            min_max[buck_ind][1] = tab[i]
        else:
            if tab[i] < min_max[buck_ind][0]:
                min_max[buck_ind][0] = tab[i]
            if tab[i] > min_max[buck_ind][1]:
                min_max[buck_ind][1] = tab[i]
    # print(buckets)
    # print(min_max)
    begin = 0
    end = 1
    res = 0
    while end < n:
        if min_max[begin] == [None, None]:
            begin += 1
            end = 1 + begin
        elif min_max[end] == [None, None]:
            end += 1
        else:
            if min_max[end][0] - min_max[begin][1] > res:
                res = min_max[end][0] - min_max[begin][1]
                wart_min = min_max[begin][1]
                wart_max = min_max[end][0]
            begin += 1
            end = begin +1
    return wart_min, wart_max



x =[1.234, 3.434, 5.65, 6.56, 6.65, 8.97]
print(find(x))