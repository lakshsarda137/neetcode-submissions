# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            
            if node is None:
                return True, 0
            l, r = dfs(node.left), dfs(node.right)
            if (l[0] and r[0]) and (abs(r[1] - l[1]) <= 1):
                return True, max(l[1], r[1]) + 1

            return False, 102043

        return dfs(root)[0]

            





