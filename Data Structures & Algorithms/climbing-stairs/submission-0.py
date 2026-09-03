class Solution:
    def climbStairs(self, n: int) -> int:
        #dp[i] = dp[i-1] + dp[i-2]

        dp = []
        dp.append(1)
        dp.append(2)

        for idx in range(2, n):
            dp.append(dp[idx - 1] + dp[idx - 2])

        return dp[n - 1]