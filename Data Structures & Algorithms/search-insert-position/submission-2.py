class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            #print (low, high)
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid

            elif target > nums[mid]:
                low = mid + 1

            elif target < nums[mid]:
                high = mid - 1
            #print (low, high)
        
        #low = 0, high = 5, mid = 2
        #low = 3, high = 5, mid = 4
        #low = 3, high = 3

        #low = 0, high = 4, mid = 2
        #low = 3, high = 4, mid = 3
        #low = 4, high
        return low
