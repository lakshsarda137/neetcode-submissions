class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False


        target = sum(nums) // 2

        subsets = [[], []]
        

        def dfs(i):
            
            
            if sum(subsets[0]) == sum(subsets[1]) and sum(subsets[0]) == target:
                return True
            
            if sum(subsets[0]) > target:
                return False

            if sum(subsets[1]) > target:
                return False

            for array in subsets:
                array.append(nums[i])
                if dfs(i+1):
                    return True
                array.pop(-1)
            return False
        return dfs(0)

            

            
        

