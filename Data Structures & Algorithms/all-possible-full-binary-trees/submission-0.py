class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        cache = {}
        def helper(num):
            if num == 0:
                return []

            elif num == 1:
                return [TreeNode(0, None, None)]
            elif (num % 2) == 0:
                return []

            elif num in cache:
                return cache[num]

            result = []
            for l in range(0, num): #left = 3, right = 1, n = 5
                r = num - l - 1
            
                left, right = helper(l), helper(r)
                for l_tree in left:
                    for r_tree in right:
                        result.append(TreeNode(0, l_tree, r_tree))

            cache[num] = result
            return result

        return helper(n)


            
