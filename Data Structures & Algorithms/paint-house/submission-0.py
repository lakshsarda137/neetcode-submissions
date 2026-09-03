class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        dp = []
        comp = {0: [1,2], 1: [0,2], 2:[0,1]}
        for _ in range(len(costs)):
            arr = []
            for _ in range(3):
                arr.append(float('inf'))
            dp.append(arr)

        for idx in range(3):
            dp[0][idx] = costs[0][idx]

        for row in range(1,len(costs)):
            for col in range(3):
                dp[row][col] = costs[row][col] + min(dp[row-1][comp[col][0]], dp[row-1][comp[col][1]])
        length = len(costs)
        return min(dp[length - 1][0], dp[length - 1][1], dp[length - 1][2])
