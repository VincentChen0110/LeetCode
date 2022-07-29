    n = len(s)
    dp = [[False]*n for _ in range(n)]
    ans = s[0]

    for i in range(n):
        dp[i][i] = True
    
    for start in range(n-1,-1,-1):
        for end in range(start+1, n):
            if s[start]==s[end]:
                ## 2 letter or remaining is palindrome
                ## since we need to check start+1, start from end of string
                if end-start==1 or dp[start+1][end-1]:
                    dp[start][end]=True
                    if len(ans) < (end-start+1):
                        ans = s[start:end+1]
    return ans