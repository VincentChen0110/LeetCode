def platesBetweenCandles(self, s, queries):
    """
    :type s: str
    :type queries: List[List[int]]
    :rtype: List[int]
    """
    # Use Prefix Sum
    # psum, next, prev = [0] * (len(s) + 1), [float('inf')] * (len(s) + 1), [0] * (len(s) + 1)
    # res = []
    # for i, ch in enumerate(s):
    #     psum[i + 1] = psum[i] + (ch == '|')
    #     prev[i + 1] = i if ch == '|' else prev[i]
    # for i, ch in reversed(list(enumerate(s))):
    #     next[i] = i if ch == '|' else next[i + 1]
    # for q in queries:
    #     l, r = next[q[0]], prev[q[1] + 1]
    #     res.append(r - l - (psum[r] - psum[l]) if l < r else 0)
    # return res
    
    ## Use Bisect
    
    p = [i for i in range(len(s)) if s[i] == '|']
    res = []
    for f,t in queries: 
        l = bisect.bisect_left(p, f)
        r = bisect.bisect_right(p, t)
        res.append(p[r-1] - p[l] - (r-1-l) if r > l else 0)

    return res
        