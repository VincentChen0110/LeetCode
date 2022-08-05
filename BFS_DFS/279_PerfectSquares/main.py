def numSquares(self, n):
    """
    :type n: int
    :rtype: int
    """
    ## DP Approach
    # dic = [0]*(n+1)
    # dic[0], dic[1] = 0, 1
    # for i in range(2,n+1):
    #     j = 1
    #     min_now=float('inf')
    #     while j**2<=i:
    #         min_now = min(dic[i-j**2], min_now)
    #         j+=1
    #     dic[i] = min_now + 1
    # return dic[n]
    ## BFS and use of set --> O(n)
    squares = [i**2 for i in range(1, int(n**0.5)+1)]
    d, q, nq = 1, {n}, set()
    while q:
        print(q)
        for node in q:
            for square in squares:
                if node == square: return d
                if node < square: break
                nq.add(node-square)
        q, nq, d = nq, set(), d+1