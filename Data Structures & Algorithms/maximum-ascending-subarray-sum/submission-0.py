class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = 0
        curr = 0
        for idx in range(0, len(nums)):
            if idx > 0:
                if curr > 0:
                    if nums[idx] > nums[idx - 1]:
                        curr += nums[idx]
                        max_sum = max(curr, max_sum)

                    else:
                        max_sum = max(curr, max_sum)
                        curr = nums[idx]
                else:
                    curr += nums[idx]
                    max_sum = max(curr, max_sum)

            else:
                curr += nums[idx]
                max_sum = max(curr, max_sum)
            
        return max(curr, max_sum)
                