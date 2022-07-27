def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x:x[0])
    ans = []
    for item in intervals:
        if ans and ans[-1][1] >= item[0]:
            ans[-1][1] = max(ans[-1][1],item[1])
        else:
            ans.append(item)
    return ans