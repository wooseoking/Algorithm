def dp(money):
    n = len(money)
    dp = [[0]*2 for _ in range(n)]
    
    dp[0][0] = 0
    dp[0][1] = money[0]
    
    for i in range(1,n):
        dp[i][0] = max(dp[i-1][0],dp[i-1][1])
        dp[i][1] = dp[i-1][0] + money[i]
    
    return max(dp[n-1][0],dp[n-1][1])
def solution(money):
    answer = max(dp(money[1:]),dp(money[:-1]))
    return answer