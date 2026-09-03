import collections
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        index = 0
        stack = deque()

        while index < len(tokens):
            char = tokens[index]
            if char == "+" or char == "-" or char == "*" or char == "/":
                first = stack.pop()
                second = stack.pop()
                
                if char == "+":
                    stack.append(first + second)

                elif char == "-":
                    stack.append(second - first)

                elif char == "*":
                    stack.append(first * second)

                elif char == "/":
                    stack.append(int(second/first))


            else:
                
                stack.append(int(char))
            #print (stack)
            index += 1

        return int(stack[0])