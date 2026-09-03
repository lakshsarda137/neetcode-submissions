class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set() #This is a set of tuples 
        def dfs(r, c):
            #Handling all out of bounds cases
            if r == len(grid) or c == len(grid[0]) or r < 0 or c < 0 or grid[r][c] == "0" or (r,c) in visited:
                return 


            visited.add((r,c))
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
            return
        
        result = 0

        for row in range(len(grid)):

            for col in range(len(grid[0])):

                if grid[row][col] == "1" and (row, col) not in visited:
                    dfs(row, col)
                    result += 1
                    visited.add((row, col))
        return result

