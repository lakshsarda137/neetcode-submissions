class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        cache = {}
        cache[0] = nums[0]
        best = cache[0]
        for i in range(1, len(nums)):
            cache[i] = max(cache[i - 1] + nums[i], nums[i])
            best = max(cache[i], best)

        return best