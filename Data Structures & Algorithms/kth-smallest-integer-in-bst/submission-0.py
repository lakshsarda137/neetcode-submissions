# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []
        def dfs(node):
            nonlocal result
            if not node:
                return

            dfs(node.left)
            result.append(node.val)
            dfs(node.right)
            return

        dfs(root)
        return result[k - 1]