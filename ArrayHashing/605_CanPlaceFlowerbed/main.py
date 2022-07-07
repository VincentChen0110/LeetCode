
def canPlaceFlowers(self, flowerbed, n):
    """
    :type flowerbed: List[int]
    :type n: int
    :rtype: bool
    """
    ## iterate through the flower pots
    ## Conditions: if (left is start) or (right is end) or (left,right==0) and 0: okay
    # flowerbed.insert(0, 0)
    # flowerbed.append(0)
    # count = 0
    # for f in flowerbed:
    #     if f == 0:
    #         count += 1
    #     else:
    #         count = 0
    #     if count == 3:
    #         n -= 1
    #         count = 1
    #     if n == 0:
    #         return True
    # return False
    for i, x in enumerate(flowerbed):
        if (not x and (i == 0 or flowerbed[i-1] == 0) 
                and (i == len(flowerbed)-1 or flowerbed[i+1] == 0)):
            n -= 1
            flowerbed[i] = 1
    return n <= 0
flowerbed = [1,0,0,0,1]
n = 2
print(canPlaceFlowers(flowerbed,n))