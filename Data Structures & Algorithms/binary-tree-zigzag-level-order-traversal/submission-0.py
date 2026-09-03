class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return []

        q = deque([root])
        left_to_right = True

        while q:
            level_size = len(q)
            level_nodes = []
            for _ in range(level_size):
                node = q.popleft()
                level_nodes.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            
            if not left_to_right:
                level_nodes.reverse()
            result.append(level_nodes)
            left_to_right = not left_to_right
            
        return result