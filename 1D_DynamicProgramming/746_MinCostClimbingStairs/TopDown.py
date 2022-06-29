def minCostStairs(cost)
    def util(cost, index):

        if index in memo:
            return memo[index]
        if index >= len(cost):
            return 0

        memo[index] =  cost[index] + min(util(cost, index+1), util(cost, index+2))
        return memo[index]

    memo = {}
    return min(util(cost, 0),util(cost, 1) ) 