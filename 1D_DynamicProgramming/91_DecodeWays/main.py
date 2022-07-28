def numDecodings(self, s):
    """
    :type s: str
    :rtype: int
    """
    ### SubProblem: ans[i] = ans[i-1] + s[i]
    ans = [0 for _ in range(len(s)+1)]
    ans[0] = 1
    ans[1] = 0 if s[0]=='0' else 1
    
    for i in range(2,len(s)+1):
        if 0<int(s[i-1:i])<=9:
            ans[i] += ans[i-1]
        if 10<=int(s[i-2:i])<= 26:
            ans[i] += ans[i-2]
    return ans[-1]