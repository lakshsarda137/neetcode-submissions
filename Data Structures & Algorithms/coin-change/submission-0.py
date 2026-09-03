class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        hash_set = set()
        for coin in coins:
            hash_set.add(coin)


        dp = {} #Amount: Minimum mumber of coins...
        if amount == 0:
            return 0
        for amt in range(1, amount + 1):

            mini = float('inf')
            if amt in hash_set:
                dp[amt] = 1
                mini = 1

            else:
                for coin in hash_set:
                    if (amt - coin) > 0:
                        mini = min(dp[amt - coin] + 1, mini)
            dp[amt] = mini

        if dp[amount] == float('inf'):
            return -1
        else:
            return dp[amount]

        