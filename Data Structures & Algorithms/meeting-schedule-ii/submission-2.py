import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x:x.start)
        if len(intervals) == 0:
            return 0

        elif len(intervals) == 1:
            return 1
        rooms = [intervals[0].end]  # min-heap of end times, one per room in use
        for idx in range (len(intervals)):
            interval = intervals[idx]
            if idx > 0:
                if interval.start >= rooms[0]:   # earliest-ending room is free
                    heapq.heappop(rooms)         # reuse it
                heapq.heappush(rooms, interval.end)
        return len(rooms)