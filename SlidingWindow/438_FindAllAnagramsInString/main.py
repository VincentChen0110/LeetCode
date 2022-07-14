def findAnagrams(self, s, p):
    """
    :type s: str
    :type p: str
    :rtype: List[int]
    """
    n = len(p)
    #p = sorted(p)
    dic_s, dic_p = {}, {}
    ans = []
    # for i in range(0,len(s)-n+1):
    #     if sorted(s[i:i+n])== p:
    #         ans.append(i)
    # return ans
    for c in p:
        dic_p[c] = dic_p.get(c,0)+1
    
    for i in range(0, len(s)):
        dic_s[s[i]] = dic_s.get(s[i],0) + 1
        #print(dic_s)
        ## Or you could use counter
        if dic_s == dic_p:
            ans.append(i+1-n)
        if i >= n-1:
            dic_s[s[i+1-n]] -= 1
            if dic_s[s[i+1-n]]==0: 
                dic_s.pop(s[i+1-n])
        
    return ans