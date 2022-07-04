def distributeCandies(self, candyType):
    """
    :type candyType: List[int]
    :rtype: int
    """
    n = len(set(candyType))
    if n>len(candyType)//2:
        return len(candyType)//2
    else:
        return n