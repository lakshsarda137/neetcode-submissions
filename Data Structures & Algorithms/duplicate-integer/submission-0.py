class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = {}
        for num in nums:
            if num not in counts:
                counts[num] = 1
            elif num in counts:
                counts[num] += 1
        print (counts)
        for key in counts:
            if counts[key] > 1:
                return True
        return False