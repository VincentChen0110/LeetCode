def isSubsequence(s,t):
    if len(s)>len(t): return False
    if not s: return True
    index = 0
    for c in t:
        if c==s[index]:
            index+=1
        if index==len(s):
            return True
        
    return False