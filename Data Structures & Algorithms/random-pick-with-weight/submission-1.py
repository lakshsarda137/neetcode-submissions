import random
class Solution:

    def __init__(self, w: List[int]):
       self.arr = []
       self.original = w.copy()
       self.length = 0
       for idx in range(len(w)):

        for _ in range(w[idx]):
            self.arr.append(idx)
            self.length += 1


        

    def pickIndex(self) -> int:
        choice = random.randint(0, self.length - 1)
        return self.arr[choice]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()