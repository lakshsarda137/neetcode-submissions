class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        R, C = len(grid), len(grid[0])
        visited = set()
        def dfs(r, c):

            if r < 0 or c < 0 or r >= R or c >= C or grid[r][c] == 0:
                return 0

            elif (r,c) in visited:
                return 0
            #output = 0
            elif grid[r][c] == 1 and (r,c) not in visited:
                visited.add((r,c))
                output = 1
                for vec in directions:
                    dr = vec[0]
                    dc = vec[1]
                    output = dfs(r + dr, c + dc) + output
            return output
            
        result = 0

        for row in range(R):
            for col in range(C):

                if (row, col) not in visited and grid[row][col] == 1:
                    potential = dfs(row, col)
                    result = max(potential, result)
                    # visited.add((row, col))
        return result
