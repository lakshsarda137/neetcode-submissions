from collections import deque
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        queue = deque()
        left = 0
        right = k - 1
        hash_set = set() #Contains the number of white block occurences
        #First pass
        count = 0
        while left <= right:
            char = blocks[left]
            queue.append(char)
            if char == "W":
                count += 1
            left += 1
        hash_set.add(count)
        for right in range(k, len(blocks)):
            char = blocks[left]
            queue.append(char)
            if char == "W":
                count += 1
            remove = queue.popleft()
            if remove == "W":
                count = count - 1
            
            hash_set.add(count)
            left += 1
        return min(hash_set)

            




