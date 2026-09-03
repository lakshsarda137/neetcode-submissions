import collections
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        length = len(s)
        idx = 0

        while idx < length:
            current = s[idx]
            if current == '[' or current == '(' or current == '{':
                stack.append(current)
                idx += 1

            else:
                if len(stack) == 0:
                    return False

                closer = stack.pop()
                if (closer == "[" and current == "]") or (closer == "{" and current == "}") or (closer == "(" and current == ")"):
                    idx += 1

                else:
                    return False
        if len(stack) > 0:
            return False
        return True
        