class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        def helper(i):
            result = []

            left = i + 1
            right = len(nums) - 1

            while left < right:
                if nums[left] + nums[right] + nums[i] == 0:
                    lst = [nums[i], nums[left], nums[right]]
                    result.append(lst)
                    left += 1
                    right = right - 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif nums[left] + nums[right] + nums[i] < 0:
                    left = left + 1

                else:
                    right = right - 1

            return result
        final = []

        for idx in range(0, len(nums) - 2):
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue
            inter = helper(idx)
            

            #print ("inter is: ", inter)
            if len(inter) > 0:
                for arr in inter:
                    final.append(arr.copy())
                
        return final
            






