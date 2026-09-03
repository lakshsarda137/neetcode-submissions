class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
    
        cache = []
        for rows in range(m):
            arr = []
            for cols in range(n):
                arr.append(0)

            cache.append(arr)
        
        #dp[i][j] = dp[i-1][j] + dp[i][j-1]

        for cols in range(n):
            if cols > 0:
                cache[0][cols] = cache[0][cols-1] + grid[0][cols]
            else:
                cache[0][cols] = grid[0][cols]

        for rows in range(m):
            if rows > 0:
                cache[rows][0] = cache[rows - 1][0] + grid[rows][0]
            else:
                cache[rows][0] = grid[rows][0]

        
        for i in range(m):
            for j in range(n):

                if cache[i][j] != 0:
                    continue

                else:
                    cache[i][j] = min(cache[i-1][j],cache[i][j-1]) + grid[i][j]
        #print (cache)
        return cache[m-1][n-1]

