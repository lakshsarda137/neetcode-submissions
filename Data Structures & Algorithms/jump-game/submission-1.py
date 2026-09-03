class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}
        memo[len(nums) - 1] = True
        def dfs(i):
            if i >= len(nums):
                return True
            if i in memo:
                return memo[i]
            
            for new_idx in range(i + 1, i + nums[i] + 1, 1):
                branch = dfs(new_idx)
                if branch:
                    memo[i] = True
                    return True

            memo[i] = False
            return False

        return dfs(0)

            

