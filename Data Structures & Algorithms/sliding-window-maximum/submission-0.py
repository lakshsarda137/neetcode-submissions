import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        left = 0
        right = k - 1
        result = []
        while right < len(nums):
            right = left + k - 1
            arr = nums[left: right + 1]
            arr = [-num for num in arr]
            heapq.heapify(arr)
            num = -heapq.heappop(arr)
            result.append(num)
            left += 1
            right += 1
        return result
