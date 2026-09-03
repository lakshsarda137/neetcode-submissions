class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        
        def days(candidate):
            count = 0
            for idx in range(len(piles)):
                offer = piles[idx] #This is the number of bananas I must eat
                if offer % candidate == 0:
                    count = count + offer/candidate
                    

                elif offer < candidate:
                    count += 1

                elif offer % candidate != 0 and offer > candidate:
                    count = count + offer//candidate + 1

            return count


        left = 1
        right = max(piles)
        if h == len(piles):
            return right
        best = max(piles)
        while left <= right:
            mid = (left + right) // 2
            if days(mid) > h:
                left = mid + 1

            elif days(mid) <= h:
                best = mid
                right = mid - 1

            
        return best


        

        

        

