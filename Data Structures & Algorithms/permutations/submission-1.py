class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []

        def dfs(i, chain):
            if len(chain) == len(nums):
                result.append(chain.copy())
                return

            for idx in range(len(chain) + 1):
                new_chain = chain[0:idx] + [nums[i]] + chain[idx:]
                dfs(i+1, new_chain)
            return

        dfs(0, [])
        return result
