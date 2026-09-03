class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = deque()
        for idx in range(len(temperatures)):
            temp = temperatures[idx]

            while stack and temp > stack[-1][0]:
                top = stack.pop()
                result[top[1]] = (top[1] - idx) * -1

            stack.append((temp, idx))

        return result


