import collections
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(1,0), (0,1), (0,-1), (-1,0)]
        R, C = len(grid), len(grid[0])
        visited = set()
    

        def bfs(row, col):
            """
            row: an integer representing idx of row
            col: an integer representing idx of col

            row, col is the coordinate of an unvisited island

            The goal is to keep updating the visited set until the island breaks
            """

            if (row, col) in visited: #Bad coords given, termiante
                return
            q = collections.deque()
            q.append((row, col))
            visited.add((row, col))

            while q:
                current = q.popleft()
                #print (len(q))
                for vector in directions:
                    x = current[0] + vector[0]
                    y = current[1] + vector[1]

                    if x < 0 or y < 0 or x == R or y == C:
                        continue

                    elif (x,y) in visited:
                        continue

                    elif grid[x][y] == "0":
                        #visited.add((x, y))
                        continue

                    elif grid[x][y] == "1":
                        visited.add((x, y))
                        q.append((x, y))

            return
        result = 0
        for row_idx in range(R):
            for col_idx in range(C):
                if grid[row_idx][col_idx] == "1" and (row_idx, col_idx) not in visited:
                    bfs(row_idx, col_idx)
                    result += 1
                elif grid[row_idx][col_idx] == "0":
                    visited.add((row_idx, col_idx))

        return result





        
                    







