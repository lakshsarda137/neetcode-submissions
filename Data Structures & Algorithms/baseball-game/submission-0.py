class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = []

        iterations = 0
        idx = 0
        while iterations < len(operations):
            #print (result, idx)
            current = operations[iterations]
            # print ("current: ", current)
            if current == "+":
                result.append(result[idx-1] + result[idx-2])
                idx += 1

            elif current == "D":
                result.append(result[idx-1] * 2)
                idx += 1
            
            elif current == "C":
                result.pop(-1)
                idx = idx - 1

            else:
                result.append(int(current))
                idx += 1
            iterations += 1

        return sum(result)

            

            
