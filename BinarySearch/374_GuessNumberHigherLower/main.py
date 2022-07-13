def guessNumber(self, n):
    """
    :type n: int
    :rtype: int
    """
    l ,r = 1, n
    while(l<=r):
        m = l+(r-l)//2
        if(guess(m)==0):return m
        elif(guess(m)==-1):r = m-1
        else: l = m+1
    return l