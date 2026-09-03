class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            top = -heapq.heappop(maxHeap)
            second = -heapq.heappop(maxHeap)
            if top == second:
                continue

            else:
                heapq.heappush(maxHeap, second - top)

        if len(maxHeap) == 1:
            value = heapq.heappop(maxHeap)
            return -value

        else:
            return 0