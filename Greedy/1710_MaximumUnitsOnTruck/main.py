def maximumUnits(self, boxTypes, truckSize):
    """
    :type boxTypes: List[List[int]]
    :type truckSize: int
    :rtype: int
    """
    boxvalue = sorted(boxTypes, key = lambda x: x[1], reverse = True)
    ans = 0
    for box in boxvalue:
        if truckSize > box[0]:
            ans += box[0]*box[1]
            truckSize-=box[0]
        else:
            ans+=truckSize*box[1]
            return ans
    return ans