# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        total = 0
        def dfs(node):
            if not node:
                return 0

            if node.val >= low and node.val <= high:

                left = dfs(node.left)
                right = dfs(node.right)
                return left + right + node.val

            else:
                left, right = dfs(node.left), dfs(node.right)

                return left + right

        return dfs(root)
    