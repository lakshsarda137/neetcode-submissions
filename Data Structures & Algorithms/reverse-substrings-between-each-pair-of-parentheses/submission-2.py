import sys
sys.setrecursionlimit(5000)
class Solution:
    def reverseParentheses(self, s: str) -> str:
        def helper(string):
         
            if "(" not in string: #Need to just reverse the string - no recursion
                return string

            #If I'm here, then that means I am looking at something nested or stuff like (ab)(cd). Depth tracking might help

            start_idx = [] #List of all starting (
            end_idx = [] #List of all ending ). Synchronised with start_idx for better parsability


            depth = 0 #the depth i truly care about

            for i in range(0, len(string), 1):
                char = string[i]
                if char == "(" and depth == 0:
                    start_idx.append(i)
                    depth += 1
                elif char == "(" and depth > 0:
                    depth += 1
                elif char == ")" and depth == 1:
                    
                    end_idx.append(i)
                    depth -= 1
                elif char == ")" and depth > 1:
                    depth -= 1

            #if i had z(ab)(cd)e, i'd want z + f(ab) + f(cd) + e
        
            final_string = ""
            master_idx = 0
            for i in range(0, len(start_idx)):
                start, end = start_idx[i], end_idx[i]
                final_string = final_string + string[master_idx:start] + helper(string[start + 1:end])[::-1]
               
                master_idx = end + 1

            final_string = final_string + string[master_idx:]
           

            return final_string



        return helper(s)