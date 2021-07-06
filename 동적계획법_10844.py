N = int(input())

dp = [[0] * 10 for _ in range(N + 1)]

for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, N + 1):
    dp[i][0] = dp[i-1][1]
    dp[i][1] = dp[i-1][0] + dp[i-1][2]
    dp[i][2] = dp[i-1][1] + dp[i-1][3]
    dp[i][3] = dp[i-1][2] + dp[i-1][4]
    dp[i][4] = dp[i-1][3] + dp[i-1][5]
    dp[i][5] = dp[i-1][4] + dp[i-1][6]
    dp[i][6] = dp[i-1][5] + dp[i-1][7]
    dp[i][7] = dp[i-1][6] + dp[i-1][8]
    dp[i][8] = dp[i-1][7] + dp[i-1][9]
    dp[i][9] = dp[i-1][8]

count = 0
for i in range(10):
    count += dp[-1][i]

print(count % 1000000000)
