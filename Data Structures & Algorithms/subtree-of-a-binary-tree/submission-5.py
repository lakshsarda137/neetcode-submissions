# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def sametree(n1, n2):
            if n1 is None and n2 is None:
                return True
            elif n1 is not None and n2 is None:
                return False

            elif n1 is None and n2 is not None:
                return False

            elif n1.val != n2.val:
                return False

            return sametree(n1.left, n2.left) and sametree(n1.right, n2.right)

        def dfs(main, sub):
            if main is None and sub is None:
                return True

            elif main is not None and sub is None:
                return False

            elif main is None and sub is not None:
                return False

            elif main.val == sub.val:
                potential = sametree(main, sub)
                if potential:
                    return True

                else:
                    return dfs(main.left, sub) or dfs(main.right, sub)

            elif main.val != sub.val:
                return dfs(main.left, sub) or dfs(main.right, sub)
                

        return dfs(root, subRoot)