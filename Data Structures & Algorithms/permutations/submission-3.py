class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        length = len(nums)
        def dfs(i, chain):
            if len(chain) == length:
                result.append(chain.copy())
                return

            for idx in range(len(chain)+1):
                if nums[i] not in chain:
                    chain = chain[0:idx] + [nums[i]] + chain[idx:]
                    dfs(i+1, chain)
                    chain = chain[0:idx] + chain[idx+1:] #backtrack

            return

        dfs(0, [])
        return result