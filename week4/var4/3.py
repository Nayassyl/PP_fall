def bunny():
    n = int(input())
    while n:
        a = (int(i) for i in input().split())
        dp = [0 for i in range(len(a))]
        dp[0] = a[0]
        dp[1] = a[0]
        dp[2] = a[0] + a[2]
        for i in range(3, n):
            dp[i] = max(dp[i - 2], dp[i - 3]) + a[i]
        print(max(dp[n-1], dp[n-2]))
        n -= 1

bunny()