
from collections import deque
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash_map = {}
        for idx in range(len(nums2)):
            hash_map[nums2[idx]] = idx
        result = []
        for i in range(len(nums1)):
            number = nums1[i]
            left = hash_map[number]
            put = -1
            for right in range(left + 1, len(nums2)):
                if nums2[right] > number:
                    put = nums2[right]
                    result.append(put)
                    break
            if put == -1:
                result.append(-1)
        return result
