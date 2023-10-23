n = int(input())
def fibbo(n):
    dp = [0 for i in range(n)]
    dp[1] = 1
    x = lambda a: a ** 3
    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]
    for elem in dp: print(x(elem), end = " ")
fibbo(n)


