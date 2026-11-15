class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        R, C = len(matrix), len(matrix[0])

        cache = [[float('inf')] * C for _ in range(R)]

        for c in range(0, C, 1):
            cache[R - 1][c] = matrix[R - 1][c]


        def dfs(r, c):
            if r < 0 or c < 0 or r >= R or c >= C:
                return float('inf')

            elif cache[r][c] != float('inf'):
                return cache[r][c]

            cache[r][c] = min(
                dfs(r + 1, c),
                dfs(r + 1, c - 1),
                dfs(r + 1, c + 1)
            ) + matrix[r][c]
            return cache[r][c]

        result = float('inf')

        for c in range(0, C):
            result = min(result, dfs(0, c)) 

        return result