class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()
        def dfs(i, goal, branch):
            if goal == 0:
                result.append(branch.copy())
                return

            elif i == len(nums) or goal < 0:
                return

            while i > 0 and i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1

            for idx in range(i, len(nums)):
                branch.append(nums[idx])
                dfs(idx, goal - nums[idx], branch.copy())
                branch.pop()

            return
        dfs(0, target,[])
        return result


            



                

