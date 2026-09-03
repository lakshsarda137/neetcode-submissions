# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0
        def dfs(node):
            nonlocal result
            if node is None:
                return -1

            left = 1 + dfs(node.left)
            right = 1 + dfs(node.right)
            result = max(result, left + right)
            return max(left, right)
        dfs(root)
        return result
   



