def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        heap = [-x for x in stones]
        heapq.heapify(heap)
        while len(heap)>1:
            y = heapq.heappop(heap)
            x = heapq.heappop(heap)
            if x!=y: heapq.heappush(heap,y-x)
        if len(heap)==0: return 0  
        return -heap[0]