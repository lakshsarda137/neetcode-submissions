import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for point in points:
            tup = ((point[0])**2 + (point[1])**2, point[0], point[1])
            distances.append(tup)
        heapq.heapify(distances)
        result = []
        for _ in range(k):
            current = heapq.heappop(distances)
            med = [current[1], current[2]]
            result.append(med)

        return result


