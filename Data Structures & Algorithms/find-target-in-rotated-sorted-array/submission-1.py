class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binary_search(left, right):

            while left <= right:

                mid = (left + right) // 2
                if target > nums[mid]:
                    left = mid + 1

                elif target < nums[mid]:
                    right = mid - 1

                elif target == nums[mid]:
                    return mid

            return -1

        def pivot_find(array):
            left, right = 0, len(array) - 1

            if array[left] < array[right]:
                return 0

            while left <= right:
                mid = (left + right) // 2
                if array[left] > array[mid]:
                    right = mid

                elif array[right] < array[mid]:
                    left = mid + 1
                else:
                    return left

                

            return left

        pivot = pivot_find(nums)

        output1 = binary_search(0, pivot - 1)
        if output1 != -1:
            return output1

        else:
            return binary_search(pivot, len(nums) - 1)

