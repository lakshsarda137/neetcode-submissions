class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        best = -len(s) - 1

        left = 0
        hash_set = set()
        for right in range (len(s)):

            if s[right] not in hash_set:
                hash_set.add(s[right])
                best = max(best, right - left + 1 )

            else:
                while s[right] in hash_set:
                    print (hash_set, " and s right was, ", s[right])
                    hash_set.remove(s[left])
                    left = left + 1
                hash_set.add(s[right])
        if best < 0:
            return 0
        else:
            return best

