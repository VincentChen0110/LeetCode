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
        ## In other words, check if the numbers of not maxfreq character is larger than k (j-i+1-best>k)
        if best + k < j-i+1:
            count[s[i]]-=1 ##since we are going to shift our window, the dic will also be updated
            i+=1 ## Shift start index
        ans = max(ans, j -i+1)
    return ans