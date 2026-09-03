# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        low = 1
        high = n

        mid = n // 2 + 1
        result = 2
        while result != 0:
            result = guess(mid)

            if result == -1:
                high = mid - 1
            if result == 1:
                low = mid + 1
            if result == 0:
                return mid
            mid = (low + high) // 2

