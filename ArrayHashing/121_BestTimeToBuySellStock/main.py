
def  maxProfit(self, prices):
    ans, minimum = 0, float('inf')
    for p in prices:
        minimum = min(minimum, p)
        ans = max(p-minimum, ans)
    return ans