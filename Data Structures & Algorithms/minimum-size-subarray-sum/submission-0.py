class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        best = float('inf')
        left = 0
        total = 0
        
        for right in range (0,len(nums)):
            total += nums[right]
            while total >= target:
                total = total - nums[left]
                best = min(right - left + 1, best)
                left = left + 1

        return 0 if best == float('inf') else best
                
                
                

            

        
            
