class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        balloons = []
        for c in colors:
            balloons.append(c)

        cache = {}
        cache[0] = 0
        for i in range(1, len(colors), 1):
            if balloons[i] == balloons[i - 1]:
                #Now we are inside the recursive case. I first want to know if a swap should happen

                if neededTime[i] < neededTime[i - 1]:
                    cache[i] = cache[i - 1] + neededTime[i]
                    tmp = neededTime[i]
                    neededTime[i] = neededTime[i - 1]
                    neededTime[i - 1] = tmp
                else: #No swap needed
                    cache[i] = cache[i - 1] + neededTime[i - 1]
                
            else:
                cache[i] = cache[i - 1]

        return cache[len(colors) - 1]

