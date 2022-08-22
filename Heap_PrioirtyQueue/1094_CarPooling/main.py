def carPooling(self, trips, capacity):
    """
    :type trips: List[List[int]]
    :type capacity: int
    :rtype: bool
    """
    # trips = [[9,3,4],[9,1,7],[4,2,4],[7,4,5]]
    # capacity = 23
    # start = [(b,1,a) for a,b,c in trips]
    # end = [(c,0,a) for a, b, c in trips]
    # total = start+end
    # total.sort()
    # # print(total)
    # for trip in total:
    #     if trip[1]==1:
    #         capacity-=trip[2]
    #         if capacity < 0:
    #             return False
    #     if trip[1]==0:
    #         capacity += trip[2]
    #     # print(capacity)
    # return True
    lst = []
    for n, start, end in trips:
        lst.append((start, n))
        lst.append((end, -n))
    lst.sort()
    for loc in lst:
        capacity -= loc[1]
        if capacity < 0:
            return False
    return True