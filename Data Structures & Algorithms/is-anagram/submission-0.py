class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        #Build separate dictionaries
        string1 = {}
        string2 = {}
        for char in s:
            if char in string1:
                string1[char] += 1
            else:
                string1[char] = 1

        for char in t:
            if char in string2:
                string2[char] += 1
            else:
                string2[char] = 1

        for key in string1:
            if key not in string2:
                return False
            elif key in string2:
                if string1[key] != string2[key]:
                    return False

        return True