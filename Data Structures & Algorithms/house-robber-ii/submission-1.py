class Solution:
    def rob(self, nums: List[int]) -> int:
        cache1 = {}
        cache2 = {}
        if len(nums) == 1:
            return nums[0]

        elif len(nums) == 2:
            return max(nums[0], nums[1])

        elif len(nums) == 3:
            return max(nums[0], nums[1], nums[2])
        length = len(nums)
        cache1[0] = nums[0]
        cache1[1] = max(nums[0], nums[1])
        for i in range(2, len(nums) - 1):
            cache1[i] = max(cache1[i - 2] + nums[i], cache1[i - 1])

        cache2[1] = nums[1]
        cache2[2] = max(nums[1], nums[2])

        for i in range(3, len(nums)):
            cache2[i] = max(cache2[i - 2] + nums[i], cache2[i - 1])

        return max(cache1[length - 2], cache2[length - 1])

        
            





