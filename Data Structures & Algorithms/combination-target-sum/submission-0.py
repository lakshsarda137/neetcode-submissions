class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # if sum(nums) < target:
        #     return []
        
        def helper(start, branch = [], tgt = target, overall = []):
            if tgt == 0:
                overall.append(branch.copy())
                return overall

            elif tgt < 0:
                return overall

            for index in range (start, len(nums)):
                branch.append(nums[index])
                chance = helper(index, branch, tgt - nums[index], overall)
                
                branch.pop(-1)
            return overall
        return helper(0, [], target)
        

                

