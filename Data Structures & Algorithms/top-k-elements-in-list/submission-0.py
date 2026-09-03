class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = len(nums) * [0]
        #The goal is to create an array where count[i] = elements that
        #appear i times in the array, nums


        hash_map = {}
        for num in nums:
            if num not in hash_map:
                hash_map[num] = 1
            else:
                hash_map[num] += 1
        
        for key in hash_map:
            freq = hash_map[key] #The number, key, appeared freq times
            #in the array, nums. 

            if count[freq-1] == 0:
                count[freq-1] = [key]
            else:
                count[freq-1].append(key)
        remaining = k
        output = []
        for idx in range (len(count) - 1, -1, -1):
            if count[idx] != 0:
                output = output + count[idx]
                remaining = remaining - len(count[idx])

            if remaining == 0:
                return output
        





        

                

        
