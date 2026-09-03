# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:


        def dfs(node, rem):

            if node is None:
                return False
            elif node.left is None and node.right is None and rem == node.val:
                return True

            elif node.left is None and node.right is None and rem != node.val:
                return False



            return dfs(node.left, rem - node.val) or dfs(node.right, rem - node.val)
        return dfs(root, targetSum)
        