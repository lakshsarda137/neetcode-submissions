class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        prefix = [1] * n
        for i in range (1, n):
            prefix[i] = prefix[i - 1] * nums[i-1]

        suffix = [1] * n
        for i in range (n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i+1]

        output = []

        for i in range (0, n):
            output.append(suffix[i] * prefix[i])

        return output