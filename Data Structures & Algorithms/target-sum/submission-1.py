class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sm = sum(nums)
        if sm < abs(target):
            return 0
        dp = []

        for row in range(len(nums)):
            arr = []
            for col in range(-sm, sm + 1, 1):
                arr.append(0)
            dp.append(arr.copy())

        dp[0][nums[0] + sm] += 1
        dp[0][-nums[0] + sm] += 1

        for r in range(1, len(nums)):
            for c in range(-sm, sm + 1, 1):
                if c - nums[r] >= -sm:
                    dp[r][c + sm] += dp[r - 1][c - nums[r] + sm]
                if c + nums[r] <= sm:
                    dp[r][c + sm] += dp[r - 1][c + nums[r] + sm]

        return dp[len(nums) - 1][target + sm]