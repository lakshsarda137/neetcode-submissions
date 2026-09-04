class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R, C = len(heights), len(heights[0])
        pac, atl = set(), set()
        #visited = set()

        result = []
        def dfs(r, c, visit, height):
            if (r,c) in visit:
                return

            if r < 0 or c < 0 or r >= R or c >= C or heights[r][c] < height:
                return

            visit.add((r,c))
            new_height = heights[r][c]
            dfs(r + 1, c, visit, new_height), dfs(r, c + 1, visit, new_height), dfs(r - 1, c, visit, new_height), dfs(r , c - 1, visit, new_height)
            return


        for row in range(R):
            #pac.add((row, 0))
            dfs(row, 0, pac, heights[row][0])
            #atl.add((row, C - 1))
            dfs(row, C - 1, atl, heights[row][C - 1])
            
        for col in range(C):
            #pac.add((0, col))
            dfs(0, col, pac, heights[0][col])
            #atl.add((R - 1, col))
            dfs(R - 1, col, atl, heights[R - 1][col])

        for row in range(R):
            for col in range(C):
                if (row, col) in pac and (row, col) in atl:
                    arr = [row, col]
                    result.append(arr.copy())

        return result
        


