class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

       #pascal(i,j) = pascal(i-1, j-1) + pascal(i-1, j)
       #if j == 0, pascal(i,j) = 1
       #if j == numsrows-1, then pascal(i,j) = 1

        pascal = []
        for count in range(numRows):
            pascal.append([])
        
        
        for i in range(numRows):

            for j in range(0, i + 1):

                pascal[i].append(0)
        
        for i in range (numRows):

            for j in range(0, i + 1):

                if j == 0:
                    pascal[i][j] = 1
                if j == i:
                    pascal[i][j] = 1

        for i in range(numRows):

            for j in range (i+1):
                if pascal[i][j] == 0:
                    pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
        return pascal