class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        result = 0
        left = 0
        right = 0
        running_sum = 0
        while right < len(arr):
            
            if (right - left + 1) == k:
                running_sum += arr[right]
                if running_sum/k >= threshold:
                    result += 1
                    running_sum = running_sum - arr[left]
                    left = left + 1
                    right = right + 1
                    
                    
                else:
                    running_sum = running_sum - arr[left] - arr[right]
                    left += 1

            elif (right - left + 1) < k:
                running_sum += arr[right]
                right += 1
                
                

        return result


