def topKFrequent(self, words, k):
    """
    :type words: List[str]
    :type k: int
    :rtype: List[str]
    """
    # dict = {}
    # for x in words:
    #     if x in dict:
    #         dict[x] += 1
    #     else:
    #         dict[x] = 1
    # res = sorted(dict, key=lambda x: (-dict[x], x))
    # return res[:k]
    count = collections.Counter(words)
    heap = (heapq.nsmallest(k, count.items(), key= lambda item: (-item[1], item[0])))
    return [word for word, _ in heap]