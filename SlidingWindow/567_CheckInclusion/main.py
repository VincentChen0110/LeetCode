def checkInclusion(s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    ## Sort Version
    # window_size = len(s1)
    # s1 = list(sorted(s1))
    # for i in range(0,len(s2)-window_size+1):
    #     substring = s2[i:i+window_size]
    #     if sorted(substring) == s1:
    #         return True
    # return False
    window_size = len(s1)
    dic_s1 = {}
    
    for c in s1:
        dic_s1[c] = dic_s1.get(c, 0)+1
    
    i = 0
    for j in range(0,len(s2)):
        if (j-i+1!=window_size):
            if s2[j] in dic_s1:
                dic_s1[s2[j]]-=1
        
        else: 
            if s2[j] in dic_s1:
                dic_s1[s2[j]]-=1
            if all(x==0 for x in dic_s1.values()):
                return True
            else:
                if s2[i] in dic_s1:
                    dic_s1[s2[i]]+=1
                i+=1
    return False

s1 = "ab"
s2 = "eidbaooo"

print(checkInclusion(s1,s2))