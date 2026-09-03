# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def helper(rootp, rootq):

            if rootp is None and rootq is None:
                return True
            elif rootp is None and rootq is not None:
                return False

            elif rootp is not None and rootq is None:
                return False
            elif rootp.val == rootq.val:
                left, right = helper(rootp.left, rootq.left), helper(rootp.right, rootq.right)
            
            elif rootp != rootq:
                return False

            

            return (left and right)
        return helper(p, q)