class Solution:

    def stats(self, hashmap):
        """
        Returns the alphabet which has the highest count
        and the number of non alphabet occurences in the hashmap

        (alphabet with max count, count of max count alphabet, count of 
        other alphabets)
        """
        best = -20
        alpha = ""
        rep = 0 #Number of non primary candidates
        total = 0
        for key in hashmap:
            value = hashmap[key]
            total += value
            best = max(best, value)
            alpha = key
        rep = total - best
        return alpha, best, rep 
    def characterReplacement(self, s: str, k: int) -> int:
        
        best = -len(s) - 1

        left = 0 
        hmap = {}
        seen = set()
        for right in range (len(s)):
            
            if s[right] not in hmap:
                hmap[s[right]] = 1
            else:
                hmap[s[right]] += 1

            pot, need = self.stats(hmap)[1], self.stats(hmap)[2]
            print (pot, need)
            if need > k:
                hmap[s[left]] = hmap[s[left]] - 1
                left = left + 1
                
                
            elif need <= k:
                best = max(best, pot + need)
        return best


