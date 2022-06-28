def climbStairs(self, n):
    """
    :type n: int
    :rtype: int
    """
    #### n = [n-1]+[n-2] which is exactly like fibonacci
    
    # Solution1: Top-Down TLE 
    ## Time Comlextiy: O(2^n)
    # @cache ## This can help with memoization
    # if (n==0 or n==1 or n==2): return n
    # return self.climbStairs(n-1)+self.climbStairs(n-2)
    
    Solution2: Top-Down+memoization
    # Time and Space O(n)
    def climb(n):
        if n not in memo:
            memo[n] = climb(n-1)+climb(n-2)
            return memo[n]
        else:
            return memo[n]
    memo = {1:1,2:2}
    return climb(n)
    