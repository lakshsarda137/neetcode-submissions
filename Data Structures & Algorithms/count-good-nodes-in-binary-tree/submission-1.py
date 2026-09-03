# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0

        elif root.left is None and root.right is None:
            return 1

        def dfs(node, high):
            if node is None:
                return 0
            elif node.val >= high:
                return 1 + dfs(node.left, max(high, node.val)) + dfs(node.right, max(high, node.val))
            elif node.val < high:
                return dfs(node.left, high) + dfs(node.right, high)

        return dfs(root, root.val)

                
            

        