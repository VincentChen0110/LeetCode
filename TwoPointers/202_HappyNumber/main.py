def isHappy(self, n):
    """
    :type n: int
    :rtype: bool
    """
    def next_num(num):
        return sum(map(lambda x:int(x)**2, str(num)))
    slow, fast = n, next_num(n)
    while slow != fast and fast != 1:
        slow = next_num(slow)
        fast = next_num(next_num(fast))
    return fast == 1 or not slow == fast
    
#         ans = set()
#         while n not in ans:
#             ans.add(n)
#             n = sum(int(x)**2 for x in str(n))
#             if n==1:return True
    
#         return False