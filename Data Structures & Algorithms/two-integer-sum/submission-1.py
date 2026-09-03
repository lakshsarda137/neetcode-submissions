class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapped = {}
        for idx in range (0, len(nums)):
            mapped[nums[idx]] = idx

        for idx in range (0, len(nums)):
            current_number = nums[idx]
            complement = target - current_number
            if (complement in mapped):
                if mapped[complement] != idx:

                    return [idx, mapped[complement]]