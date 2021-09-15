def insertion_sort(tab):
    for i in range(1, len(tab)):
        tmp = tab[i]
        ind = i-1
        while ind >= 0 and tmp < tab[ind]:
            tab[ind+1] = tab[ind]
            ind -= 1
        tab[ind+1] = tmp


def bucket_sort(tab):  # k - liczba kubelkow
    k = 4
    buckets = [ [] for _ in range(k)]  # tworze liste z k pustych list
    maks = max(tab)
    mini = min(tab)
    for el in tab:
        normalised = (el-mini)/maks
        buck_ind = int(k*normalised)
        print("el: ", el, " ind: ", buck_ind)
        buckets[buck_ind].append(el)
    print(buckets)
    for i in range(k):
        insertion_sort(buckets[i])
    result = []
    for i in range(k):
        result.extend(buckets[i])
    return result


# x =[1.234, 3.434, 5.65, 6.56, 6.65, 8.97, 7.8, 4.3, 9.9]
x = [2, 1, 5, 7, 5, 3, 10, 5, 10, 4, 5, 5, 5, 2, 10]
print(bucket_sort(x))