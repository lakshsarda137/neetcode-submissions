import collections
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = (2**31) - 1
        directions = [(1,0), (-1,0), (0,1), (0, -1)]
        q = deque()
        ROW, COL = len(grid), len(grid[0])
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 0:
                    q.append((i, j))
        dist = 0
        visit = set()
        while q:
            curr_length = len(q)
            dist += 1
            for _ in range(curr_length):
                row, col = q.popleft()
                if (row, col) in visit:
                    break
                visit.add((row, col))
                for dr, dc in directions:
                    x, y = dr + row, dc + col
                    if x >= 0 and x < ROW and y >= 0 and y < COL:
                        if grid[x][y] == -1:
                            visit.add((x,y))
                        elif grid[x][y] == INF:
                            grid[x][y] = dist
                            q.append((x,y))
        return 

                
                


