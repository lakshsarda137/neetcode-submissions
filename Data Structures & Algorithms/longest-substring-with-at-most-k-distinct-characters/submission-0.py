class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:

        def dict_counter(mapping):
            res = 0

            for key in mapping:
                if mapping[key] > 0:
                    res += 1

            return res <= k

        result = min(k, len(s))
        left, right = 0, 0
        hash_map = {}
        while right < len(s):
            char = s[right]
            if char in hash_map:
                hash_map[char] += 1
            else:
                hash_map[char] = 1

            
            while not dict_counter(hash_map):
                hash_map[s[left]] -= 1
                left += 1

            if dict_counter(hash_map):
                result = max(result, right - left + 1)
                right += 1
        return result


        