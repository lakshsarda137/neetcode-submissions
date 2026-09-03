class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        left = 0
        right = left + 1

        while right < len(nums):
            if (right - left) > k:
                left += 1
                right = left + 1
            else:
                if nums[left] == nums[right]:
                    return True
                else:
                    right += 1
                    
        return False
                