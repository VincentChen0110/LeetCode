def minWindow(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    if len(s)<len(t):return ""
    if s==t: return s
    
    count = len(t)
    dic_t = Counter(t)
        
    start, end = 0, 0
    ans = ''
    for end in range(len(s)):
        if (dic_t[s[end]]>0):
            count -= 1
        dic_t[s[end]]-=1
        
        while count==0:
            length = end-start+1
            if len(ans) > length or not ans:
                ans = s[start:end+1]
            dic_t[s[start]] += 1
            if dic_t[s[start]]>0:
                count +=1
            start+=1
    return ans