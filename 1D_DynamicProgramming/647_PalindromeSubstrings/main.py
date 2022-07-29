def countSubstrings(self, s):
    """
    :type s: str
    :rtype: int
    """
#         n = len(s)
#         ans = 0
#         dp = [[False]*n for _ in range(n)]
    
#         for i in range(n):
#             dp[i][i] = True
#             ans+=1
    
#         for start in range(n-1,-1,-1):
#             for end in range(start+1,n):
#                 if s[start]==s[end]:
#                     if end-start==1 or dp[start+1][end-1]:
#                         ans+=1
#                         dp[start][end] = True
#         return ans
    self.ans = 0
    def checkPalindrome(l,r):
        while l>=0 and r<len(s) and s[l]==s[r]:
            l-=1
            r+=1
            self.ans+=1
    
    for i in range(len(s)):
        checkPalindrome(i,i)
        checkPalindrome(i,i+1)
    return self.ans