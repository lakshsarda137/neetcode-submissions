class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node):
            nonlocal res
            if not node:
                return 

            

            if dfs(node.left):
                res.append(node.left.val)
            res.append(node.val)
           
           
            if dfs(node.right):
                res.append(node.val)
            return 

        dfs(root)
        return res
