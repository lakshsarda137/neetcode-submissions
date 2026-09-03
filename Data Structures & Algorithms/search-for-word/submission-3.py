class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])
        directions = [(1,0), (0,1), (-1, 0), (0,-1)]
        def dfs(r, c, visited, remaining):
            if remaining == "":
                return True
            #Out of bounds error
            elif r < 0 or c < 0 or r == R or c == C:
                return False

            elif (r,c) in visited:
                return False

            elif board[r][c] == remaining[0]:
                flags = []
                for vector in directions:
                    dr, dc = vector[0], vector[1]
                    visited.add((r, c))
                    rem = remaining[1:]
                    res = dfs(r+dr, c+dc, visited, rem)
                    flags.append(res)
                    visited.remove((r, c))
                if True in flags:
                    return True
                else:
                    return False
            return False

        for row in range(R):
            for col in range(C):

                if board[row][col] == word[0]:
                    if dfs(row, col, set(), word):
                        return True
        return False

            


            
            



            

            
