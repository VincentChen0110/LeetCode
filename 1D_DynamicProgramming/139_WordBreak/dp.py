dp = [False]*(len(s)+1)
dp[0] = True

## i to search from starting index
for i in range(len(s)):
    if dp[i]:
        ## j to search end index of word
        for j in range(i, len(s)):
            if s[i:j+1] in wordDict:
                dp[j+1] = True
return dp[-1]
## BFS