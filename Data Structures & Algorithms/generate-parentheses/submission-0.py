class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        def helper(entry = "", opening = 0, closing = 0):
            if closing > opening:
                return 
            if opening > n:
                return
            if closing > n:
                return
            if opening == n and closing == n:
                output.append(entry)
                return

            entry = entry + "("
            helper(entry, opening + 1, closing)
            entry = entry[:-1]
            entry = entry + ")"
            helper(entry, opening, closing + 1)
            return output
        return helper("", 0, 0)
