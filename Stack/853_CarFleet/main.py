def carFleet(self, target, position, speed):
    """
    :type target: int
    :type position: List[int]
    :type speed: List[int]
    :rtype: int
    """
    ### There will always be a first
    ### If the later speed surpasses, then it will always merge with first
    ### If not, then add new time
    stack = []
    for p, s in sorted(zip(position, speed))[::-1]:
        dist = float(target - p)
        if not stack:
            stack.append(dist/s)
        elif dist/s > stack[-1]:
            stack.append(dist/s)
    return len(stack)