class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = []
        for rows in range(m):
            arr = []
            for cols in range(n):
                arr.append(0)

            cache.append(arr)
        
        #dp[i][j] = dp[i-1][j] + dp[i][j-1]

        for cols in range(n):
            cache[0][cols] = 1

        for rows in range(m):
            cache[rows][0] = 1

        
        for i in range(m):
            for j in range(n):

                if cache[i][j] != 0:
                    continue

                else:
                    cache[i][j] = cache[i-1][j] + cache[i][j-1]
        #print (cache)
        return cache[m-1][n-1]

