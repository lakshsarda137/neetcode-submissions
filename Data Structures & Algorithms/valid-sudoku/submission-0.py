class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def column_checker (col_idx):
            hash_set = set()
            count = 0
            for row in range (0, 9):
                if board[row][col_idx] != ".":
                    hash_set.add(board[row][col_idx])
                    count += 1

            if len(hash_set) < count:
                return False
            return True

        def row_checker (row_idx):
            hash_set = set()
            count = 0
            for col in range (0, 9):
                if board[row_idx][col] != ".":
                    hash_set.add(board[row_idx][col])
                    count += 1

            if len(hash_set) < count:
                print ("The count was: ", count, " but the length of the set was: ", len(hash_set))
                return False
            return True

        
        def square_checker(start_x, start_y):

            hash_set = set()
            count = 0
            for right in range (3):
                for down in range (3):
                    print (start_x, start_y)
                    print ("right is: ", start_x + right, " and down is: ", start_y+down)
                    if board[start_x + right][start_y + down] != ".":
                        hash_set.add(board[start_x + right][start_y + down])
                        count += 1
            if len(hash_set) < count:
                return False
            return True

        for row in range (9):
            check = row_checker(row)
            print (check)
            if not check:
                print ("Row check killed: ", row)
                return False
        for col in range (9):
            check = column_checker(col)
            if not check:
                print ("Column check killed: ", col)
                return False
        for x in range (0, 7, 3):
            for y in range (0, 7, 3):
                check = square_checker (x,y)
                if not check:
                    return False
        return True

             