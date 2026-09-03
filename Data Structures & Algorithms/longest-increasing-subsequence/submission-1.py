class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for idx in range(1, len(nums)):
            
            for sub in range(0, idx):
                if nums[idx] > nums[sub]:
                    dp[idx] = max(dp[sub] + 1, dp[idx])

        return max(dp)