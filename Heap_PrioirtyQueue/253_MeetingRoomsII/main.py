def minMeetingRooms(self, intervals):
    """
    :type intervals: List[List[int]]
    :rtype: int
    """
    start = sorted(intervals)
    heap = []
    for item in start:
        ## if ending time passes, then allocate new room and change
        if heap and heap[0]<= item[0]:
            heapreplace(heap, item[1])
        else:
            heappush(heap,item[1])
    
    return len(heap)