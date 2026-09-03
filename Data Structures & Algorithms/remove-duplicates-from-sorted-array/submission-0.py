class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        result = 1
        set_nums = set(nums)
        length = len(set_nums)
        for idx in range(1, length):
            print (idx)
            while nums[idx] == nums[idx - 1]:
                nums.pop(idx)
            result += 1
        return result
