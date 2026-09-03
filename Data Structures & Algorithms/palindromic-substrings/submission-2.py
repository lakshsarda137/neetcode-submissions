class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = []
        for _ in range(len(s)):
            arr = []
            for _ in range(len(s)):
                arr.append(False)

            dp.append(arr)
        result = 0

        for i in range(len(s) - 1, -1, -1):
            for j in range(len(s)):
                if i > j:
                    continue

                elif i == j:
                    dp[i][j] = True
                    result += 1

                else:
                    if s[i] == s[j]:
                        if j - i == 1 or dp[i+1][j-1]:
                            dp[i][j] = True
                            result += 1
        return result
