from heapq import heapify, heappop, heappushpop
def kClosest(self, P, k):
    euclidean = lambda x, y : x*x + y*y
    for p in P:
        p.insert(0, euclidean(p[0], p[1]))
    heapify(P)
    return [heappop(P)[1:] for i in range(k)]


def kClosest(self, P, k):
    return sorted(P, key=lambda p: p[0]**2 + p[1]**2)[:k]

def kClosest(self, P, k):
    heap, euclidean = [], lambda x, y : x*x + y*y
    for i, (x, y) in enumerate(P):
        d = euclidean(x, y)
        if len(heap) == k:
            heappushpop(heap, (-d, i))     # -d to convert to max-heap (default is min)
        else: 
            heappush(heap, (-d, i))
    return [P[i] for (_, i) in heap]
