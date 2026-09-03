class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = [0] * len(nums)
        min_prod = [float('inf')] * len(nums)

        max_prod[0] = nums[0]
        min_prod[0] = nums[0]

        for idx in range(1, len(nums)):
            max_prod[idx] = max(max_prod[idx - 1] * nums[idx], nums[idx], min_prod[idx - 1] * nums[idx])
            min_prod[idx] = min(min_prod[idx - 1] * nums[idx], nums[idx], max_prod[idx - 1] * nums[idx])


        return max(max_prod)
