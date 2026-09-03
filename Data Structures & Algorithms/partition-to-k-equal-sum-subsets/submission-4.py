class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        

        def checkequal(array):

            for idx in range (1, len(array)):
                if array[idx] != array[idx - 1]:
                    return False
            return True


        def checkbalance(array, tgt):
            for idx in range(len(array)):
                if array[idx] > tgt:
                    return False
            return True

        subsets = [0] * k
        if sum(nums) % k != 0:
            return False
        
        target = sum(nums) / k

        def dfs(i):

            if i == len(nums):
                return checkequal(subsets)


            elif not checkbalance(subsets, target):
                return False

            seen = set()
            for sub in range(k):
                if subsets[sub] + nums[i] > target:
                    continue
                if subsets[sub] + nums[i] in seen:
                    continue
                subsets[sub] += nums[i]
                seen.add(subsets[sub])
                outcome = dfs(i+1)
                if outcome:
                    return True

                subsets[sub] = subsets[sub] - nums[i]

            return False
        return dfs(0)

            
                