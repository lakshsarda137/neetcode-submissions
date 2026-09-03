class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R, C = len(matrix), len(matrix[0])
        total = R * C
        left = 0
        right = total - 1

        while left <= right:
            mid = (left + right) // 2
            row = mid // C
            column = mid % C
            print ("Row is: ", row, " and col is: ", column)
            if matrix[row][column] == target:
                return True
            elif matrix[row][column] < target:
                left = mid + 1
            
            else:
                right = mid - 1

        return False
