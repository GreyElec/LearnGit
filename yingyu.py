n = 10
coin_value = [1,5,10,20,50]
dp = [[0]*(n+1) for _ in range(len(coin_value)+1)]
for i in range(len(coin_value)+1):
    dp[i][0] = 1
for i in range(n+1):
    dp[0][i] = 0
for i in range(1,len(coin_value)+1):
    for j in range(1,n+1):
        if j < coin_value[i-1]:
            dp[i][j] = dp[i-1][j]
            continue
        else:
            dp[i][j] = dp[i-1][j]+dp[i][j-coin_value[i-1]] # i == 1 对应的是1元硬币，对应的coin_value角标应该为0
