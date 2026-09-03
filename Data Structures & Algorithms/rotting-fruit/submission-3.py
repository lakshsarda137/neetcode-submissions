import collections
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(1,0), (-1,0), (0,-1), (0,1)]
        local = collections.deque()
        visited = set()
        R, C = len(grid), len(grid[0])
        fresh = 0
        for row in range(R):
            for col in range(C):

                if grid[row][col] == 2:
                    local.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        elif len(local) == 0:
            
            return -1

        def bfs(row, col, next_local):

            if (row, col) in visited:
                return next_local
            visited.add((row, col))
            for vector in directions:
                x = vector[0] + row
                y = vector[1] + col

                if x < 0 or y < 0 or x == R or y == C:
                    continue

                elif (x,y) in visited:
                    continue

                elif grid[x][y] == 0:
                    visited.add((x, y))

                elif grid[x][y] == 1:
                    next_local.append((x, y))

            return next_local
        result = 0
        for count in range(R*C + 1):
            if len(visited) == (R*C):
                break

            new = collections.deque()

            for coord in local:
                new.extend(bfs(coord[0], coord[1], collections.deque()))
            result += 1
            local.extend(new)
        if result >= (R*C + 1):
            print (result)
            return -1
        else:
            
            return result - 1
                


            


