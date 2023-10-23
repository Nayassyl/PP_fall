def binom(n, k):
    if k > n: return 'Error'
    if n == k: return 1
    if n - k == 1 or k == 1: return n
    res = 1
    if k >= n - k:
        for i in range(k + 1, n + 1): res *= i
        for i in range(1, n - k + 1): res /= i
    else: 
        for i in range(n - k + 1, n + 1): res *= i
        for i in range(1, k + 1): res /= i
    return res
n , k = [int(i) for i in input().split()]
print(binom(n, k))
