from collections import deque

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]

def maxAreaOfIsland(grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        DIR = [0, 1, 0, -1, 0]
        
        def bfs(r, c):
            q = deque([(r, c)])
            grid[r][c] = 0
            ans = 0
            while q:
                r, c = q.popleft()
                ans += 1
                for i in range(4):
                    nr, nc = r + DIR[i], c + DIR[i+1]
                    if nr < 0 or nr == m or nc < 0 or nc == n or grid[nr][nc] == 0: continue
                    grid[nr][nc] = 0  # Mark this square as visited
                    q.append((nr, nc))
            return ans
        
        ans = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    ans = max(ans, bfs(r, c))
        return ans



print(maxAreaOfIsland(grid))