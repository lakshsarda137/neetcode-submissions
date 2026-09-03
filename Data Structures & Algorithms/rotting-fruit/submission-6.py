import collections
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()

        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        visited = set()

        R, C = len(grid), len(grid[0])
        fresh = 0
        for r in range(R):
            for c in range(C):

                if grid[r][c] == 2:
                    q.append((r,c))

                elif grid[r][c] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        if len(q) == 0:
            return -1

        
        days = 0
        while q:
            length = len(q)
            days += 1
            for _ in range(length):
                coord = q.popleft()
                
                for dr, dc in directions:
                    x, y = coord[0] + dr, coord[1] + dc

                    if x < 0 or y < 0 or (x,y) in visited or x >= R or y >= C or grid[x][y] == 0:
                        visited.add((x,y))
                        continue

                    elif grid[x][y] == 1:
                        grid[x][y] = 2
                        fresh = fresh - 1
                        q.append((x, y))
                        visited.add((x,y))
                        if fresh == 0:
                            return days
                    elif grid[x][y] == 2:
                        q.append((x, y))
                        visited.add((x,y))

        return -1



        

        
                


            


