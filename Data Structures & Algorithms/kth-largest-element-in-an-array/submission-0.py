import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        new = [-num for num in nums]
        heapq.heapify(new)
        for _ in range (k):
            num = heapq.heappop(new)
        return -num