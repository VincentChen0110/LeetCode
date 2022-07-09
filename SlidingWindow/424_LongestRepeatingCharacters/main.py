def characterReplacement(self, s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    
    ### Check longest subsequence first in first Iteration
    ### 
    count = collections.Counter()
    best, i, ans = 0, 0, 0
    for j, char in enumerate(s):
        count[char]+=1 
        best = max(best, count[char])  ## Maximum freq in cur
        ## The answer should be maxf + k
        if best + k < j-i+1:
            count[s[i]]-=1
            i+=1
        ans = max(ans, j -i+1)
    return ans