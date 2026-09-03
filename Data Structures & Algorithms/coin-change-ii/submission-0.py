class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = []
        for row in range(len(coins)):
            array = []
            for cols in range(amount + 1):
                array.append(0)
            cache.append(array)

        for row in range(len(coins)):
            cache[row][0] = 1

        for i in range(len(coins)):

            for j in range(amount + 1):
                if (i - 1) >= 0 and (j - coins[i]) >= 0:
                    cache[i][j] = cache[i-1][j] + cache[i][j - coins[i]]

                elif (i - 1) >= 0 and (j - coins[i]) < 0:
                    cache[i][j] = cache[i-1][j]

                elif (i - 1) < 0 and (j - coins[i]) >= 0:
                    cache[i][j] = cache[i][j - coins[i]]
        return cache[len(coins) - 1][amount]
                    


                

        