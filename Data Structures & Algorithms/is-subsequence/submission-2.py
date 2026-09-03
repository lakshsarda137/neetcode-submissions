class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        # dp = []
        # for _ in range (len(t)):
        #     dp.append([])
        # for array in dp:
        #     for iterations in range (len(s)):
        #         array.append("")
        dp = {} #(i,j) = T/F
        if len(s) == 0:
            return True
        if len(s) > len(t):
            return False

        for i in range (len(s)):

            for j in range (len(t)):

                if i > j:
                    dp[(i,j)] = False
                if i == 0:
                    dp[(i, j)] = (j > 0 and dp[(0, j - 1)]) or s[0] == t[j]
        
        for i in range (len(s)):

            for j in range (len(t)):

                if (i, j) in dp:
                    continue
                elif i == j:
                    if s[0:i+1] == t[0: j+ 1]:
                        dp[(i,j)] = True
                    else:
                        dp[(i,j)] = False
                elif i != j:
                   
                    if dp[(i, j-1)]:
                        dp[(i,j)] = True
                    elif not dp[(i-1, j)]:
                        dp[(i,j)] = False
                    else:
                        dp[(i,j)] = dp[(i-1,j-1)] and s[i] == t[j]
                
                
        return dp[(len(s)-1, len(t)-1 )]

    
    


