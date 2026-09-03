# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        seen = set()
        count = 0
        #max_seen = 0
        def dfs(node, max_seen):
            nonlocal count
            nonlocal seen
            if node is None:
                return
            if node in seen:
                dfs(node.left, max_seen)
                dfs(node.right, max_seen)
                return

            elif node.val >= max_seen:
                seen.add(node)
                count += 1
                dfs(node.left, node.val)
                dfs(node.right, node.val)
                
                return

            else:
                seen.add(node)
                dfs(node.left, max_seen)
                dfs(node.right, max_seen)
                return

        dfs(root, -float('inf'))
        return count

                
            

        