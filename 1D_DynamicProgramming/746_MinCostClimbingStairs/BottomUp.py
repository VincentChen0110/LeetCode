def minCostClimbingStairs(cost):
    """
    :type cost: List[int]
    :rtype: int
    """

    memo = [0]*len(cost)
    memo[0], memo[1] = cost[0], cost[1]
    for i in range(2,len(cost)):
        memo[i] = cost[i] + min(memo[i-1],memo[i-2])
        
    return min(memo[-1],memo[-2])
cost = [1,100,1,1,1,100,1,1,100,1]
print(minCostClimbingStairs(cost))