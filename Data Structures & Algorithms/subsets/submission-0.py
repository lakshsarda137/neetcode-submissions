class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #[1,2] [3]
        length = len(nums)
        def helper(i, subset = [[]]):
            if i == length:
                return subset
            if i == 0:
                subset.append([nums[i]])
                return helper(i+1, subset)
            for idx in range(2 ** i):
                new_arr = subset[idx] + [nums[i]]
                
                subset.append(new_arr)
            return helper(i + 1, subset)
            
        return helper(0, [[]])