class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []
        candidates.sort()

        def dfs(i, chain):
            current_sum = sum(chain)
            if current_sum == target:
                result.append(chain.copy())
                return

            if i == len(candidates) or current_sum > target:
                return
            elif sum(chain) > target:
                return

            chain.append(candidates[i])
            dfs(i+1, chain)
            
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            chain.pop()
            dfs(i+1, chain)
            return

        dfs(0, [])
        return result        