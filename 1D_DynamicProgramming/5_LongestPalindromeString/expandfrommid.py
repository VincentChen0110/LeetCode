ans = ""
def check_palind(l,r):
    while l>=0 and r<len(s) and s[l]==s[r]:
        l-=1
        r+=1
    return s[l+1:r]
for i in range(len(s)):
    res = check_palind(i,i)
    if len(ans)<len(res):
        ans = res
    res = check_palind(i,i+1)
    if len(ans)<len(res):
        ans = res
return ans