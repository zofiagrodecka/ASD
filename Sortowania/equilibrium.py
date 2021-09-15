# Given array of integers, find equilibrium index in it.

"""For an array A consisting n elements, index i is an equilibrium index
if sum of elements of sub-array A[0..i-1] is equal to the sum of elements of sub-array A[i+1..n-1]
i.e. (A[0] + A[1] + ... + A[i-1]) = (A[i+1] + A[i+2] + ... + A[n-1]) where 0 < i < n-1
Similarly, 0 is an equilibrium index if (A[1] + A[2] + ... + A[n-1]) = 0
and n-1 is an equilibrium index if (A[0] + A[1] + ... + A[n-2]) = 0

For example, consider the array {0, -3, 5, -4, -2, 3, 1, 0}.
The equilibrium index found at index 0, 3 and 7. """


def equilibrium(A):
    n = len(A)
    sum_left = [0]*n
    res = []
    for i in range(1, n):
        sum_left[i] = sum_left[i-1] + A[i]
    if sum_left[n-2] == 0:
        res.append(0)
    sum_right = A[n-1]
    for i in range(n-3, -1, -1):
        if sum_right == sum_left[i]:
            res.append(i+1)
        else:
            sum_right += A[i+1]
    if sum_left[n - 1] - A[0] == 0:
        res.append(n - 1)
    return res


tab = [0, -3, 5, -4, -2, 3, 1, 0]
print(equilibrium(tab))
