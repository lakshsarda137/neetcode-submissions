class Solution:


    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        def dictionary_count(mapping):
            res = 0
            for key in mapping:
                if mapping[key] > 0:
                    res += 1
            return res

        
        hash_map = {}
        left, right = 0, 0

        result = min(2, len(s))
        while right < len(s):
            char = s[right]
            if char in hash_map:
                hash_map[char] += 1
            else:
                hash_map[char] = 1
            while dictionary_count(hash_map) > 2:
                
                hash_map[s[left]] -= 1
                
                left += 1
            
            
            if dictionary_count(hash_map) <= 2:
                result = max(result, right - left + 1)
                
                right += 1
        return result