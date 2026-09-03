# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q = collections.deque()

        q.append(root)
        result = []

        while q:
            local = []
            for count in range(len(q)):
                current = q.popleft()
                local.append(current.val)

                if current.left:
                    q.append(current.left)

                if current.right:
                    q.append(current.right)
            result.append(local)

        return result

            