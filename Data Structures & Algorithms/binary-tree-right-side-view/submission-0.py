# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result = []

        q = collections.deque()
        q.append(root)

        while q:
            local = []
            for _ in range(len(q)):
                current_node = q.popleft()
                local.append(current_node.val)
                if current_node.left:
                    q.append(current_node.left)

                if current_node.right:
                    q.append(current_node.right)

            result.append(local[-1])
        return result



        