from re import M



piles = [3,6,7,11]
h = 8

def minEatingSpeed(piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        Input: piles = [3,6,7,11], h = 8
        Output: 4
        """
        l,r= 1, max(piles)
        while l < r:
            m = (l + r) // 2
            if sum((p + m - 1) / m for p in piles) > h:
                l = m + 1
            else:
                r = m
        return l

print(minEatingSpeed(piles, h))
        