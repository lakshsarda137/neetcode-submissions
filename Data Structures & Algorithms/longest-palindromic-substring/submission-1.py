class Solution:
    def longestPalindrome(self, s: str) -> str:
        best = 1
        best_string = s[0]

        dp = []

        for i in range(len(s)):
            arr = []
            for j in range(len(s)):
                arr.append(False)

            dp.append(arr)

        
        for i in range(len(s) - 1, -1, -1):

            for j in range(len(s)):
                if i > j:
                    continue

                elif i == j:
                    dp[i][j] = True
                    continue
                elif s[i] == s[j] and (j - i) <= 2:
                    dp[i][j] = True
                    if (j - i + 1) > best and dp[i][j]:
                        best = j - i + 1
                        best_string = s[i:j+1]


                elif s[i] == s[j] and (j - i) > 2:
                    dp[i][j] = dp[i + 1][j - 1]
                    if (j - i + 1) > best and dp[i][j]:
                        best = j - i + 1
                        best_string = s[i:j+1]
        return best_string



