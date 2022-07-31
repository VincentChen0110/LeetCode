def coinChange(self, coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    
    ## dp algo: f(a) = f(a-c) + 1 
    ## BottomUp Method with amount as outer loop
    # max_now = amount + 1
    # dp = [0]+[max_now]*max_now
    # for i in range(1, max_now):
    #     for j in range(0,len(coins)):
    #         if coins[j] <= i:
    #             dp[i] = min(dp[i],dp[i-coins[j]]+1)
    # if dp[amount] == max_now:
    #     return -1
    # else:
    #     return dp[amount]
    
    # BottomUp Method with coins as outer loop
    max_now = amount + 1
    dp = [0]+[max_now]*max_now
    for coin in coins:
        for i in range(coin, amount+1):
            dp[i] = min(dp[i], dp[i-coin]+1)
    if dp[amount] == max_now:
        return -1
    else:
        return dp[amount]