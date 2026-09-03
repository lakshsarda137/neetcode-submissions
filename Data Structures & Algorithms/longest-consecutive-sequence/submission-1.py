class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        best = 0
        for num in nums_set:
            #Can num be the start of a sequence?
            flag = True #Do I have a reason to continue?
            count = 1
            while flag:
                if (num + 1) in nums_set:
                    count += 1 #The sequence must continue
                    num += 1
                if (num + 1) not in nums_set:
                    flag = False
            if count > best:
                best = count
        return best

            


