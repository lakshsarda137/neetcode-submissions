class Solution:
    def partition(self, s: str) -> List[List[str]]:
        output = []


        def helper(idx, branch):
            if idx == len(s):
                output.append(branch.copy())
                return output
            
            last_string = branch[-1] #This is the string at the end of branch
            #branch = ["a", "ab"], new character = "c"
            extend = last_string + s[idx] #abc
            
            array1, array2 = branch.copy(), branch.copy()
            array1[-1] = extend #branch = ["a", "abc"]
            array2.append(s[idx])
            case1, case2 = helper(idx + 1, array1.copy()), helper(idx + 1, array2.copy())
            # output.append(case1)
            # output.append(case2)
            #print ("output, ", output)
            
            return output


        stuff = helper(1, [s[0]])
        final = []
        for upper in stuff:
            flag = True
            for lower in upper:
                if lower != lower[::-1]:
                    flag = False
            if flag:
                final.append(upper)
        return final


        
        


