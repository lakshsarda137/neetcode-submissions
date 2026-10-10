class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = len(s) - 1
        
        can_we_return = False
        right_idx = float('inf')
        for idx in range(length, -1, -1):
            if s[idx] == " " and can_we_return:
                return len(s[right_idx:idx:-1])

            elif s[idx] != " " and not can_we_return:
                right_idx = idx
                can_we_return = True
        return 1

        

