def canAttendMeetings(self, intervals):
    """
    :type intervals: List[List[int]]
    :rtype: bool
    """
    if not intervals: return True
    start = sorted(intervals)
    end_time = start[0][1]
    for s, e in start[1:]:
        if s >= end_time:
            end_time = e
        else:
            return False
    return True