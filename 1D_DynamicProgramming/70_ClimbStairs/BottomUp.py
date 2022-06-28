def climbStairs(n):    
    # Solution3: Bottom-up DP
    # Time and Space O(n), Space able to opitmize to O(1)
    if n==1 or n==2: return n
    dp = [-1]*(n+1)
    dp[1], dp[2] = 1,2
    for i in range(3,n+1):
        dp[i] = dp[i-1]+dp[i-2]
    return dp[n]