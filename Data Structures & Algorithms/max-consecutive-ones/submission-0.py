class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_seen = 0
        curr_count = 0
        for num in nums:
            if num == 1:
                curr_count += 1

            else:
                max_seen = max(curr_count, max_seen)
                curr_count = 0

        return max(max_seen, curr_count)
