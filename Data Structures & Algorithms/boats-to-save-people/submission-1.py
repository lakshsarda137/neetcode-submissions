class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        arr = sorted(people)
        #1,2,2,3,3 with a limit of 3
        #1,1,4,5 with a limit of 6
        #Greedy strategy is to make sure each boat is filled to limit
        #OR maybe fill fat people first?
        count = 0
        left = 0
        right = len(people) - 1

        while left <= right:
            if arr[left] + arr[right] <= limit:
                left = left + 1
                right = right - 1
                count = count + 1
            else:
                right = right - 1
                count = count + 1
        return count 
            

