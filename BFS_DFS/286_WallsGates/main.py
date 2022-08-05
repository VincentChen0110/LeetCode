def wallsAndGates(self, rooms):
    """
    :type rooms: List[List[int]]
    :rtype: None Do not return anything, modify rooms in-place instead.
    """
    ### Depth First Search
#         def dfs(rooms, r, c, d):
#                 for x, y in [(-1,0), (1,0), (0,-1), (0,1)]:
#                     if 0 <= r+x < len(rooms) and 0 <= c+y < len(rooms[0]) and rooms[r+x][c+y] > rooms[r][c]:
#                         rooms[r+x][c+y] = d + 1
#                         dfs(rooms, r+x, c+y, d+1)

#         if not rooms:
#             return []
#         for r in range(len(rooms)):
#             for c in range(len(rooms[0])):
#                 if rooms[r][c] == 0:
#                     dfs(rooms, r, c, 0)

        ### Breadth First Search
    if not rooms:
        return []
            # Initialize the queue with all 0s
    R, C = len(rooms), len(rooms[0])
    q = collections.deque()
    for r in range(R):
        for c in range(C):
            if rooms[r][c] == 0:
                q.append((r, c))
    while q:
        r, c = q.popleft()
        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if 0<= r+x < R and 0<=c+y <C and rooms[r+x][c+y] > rooms[r][c]:
                rooms[r+x][c+y] = rooms[r][c]+1
                q.append((r+x,c+y))