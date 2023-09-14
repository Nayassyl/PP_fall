def arr(m, n):
    b = [[0 for j in range(n)] for i in range(m)]
    for i in range(m):
        for j in range(n):
            b[i][j] = i * j

    return b

n , m = [int(i) for i in input().split()]
print(arr(n, m))
