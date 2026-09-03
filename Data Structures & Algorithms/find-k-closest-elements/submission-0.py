import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        distances = []
        for num in arr:
            distances.append((abs(x - num), num))
        
        heapq.heapify(distances)
        res = []
        for _ in range (k):
            element = heapq.heappop(distances)[1]
            res.append(element)
        res.sort()
        return res