# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        working = []
        def bfs(node: Optional[TreeNode], depth: int) -> None:
            if depth >= len(working):
                working.append([])
            working[depth].append(node.val)

            if node.left:
                bfs(node.left, depth + 1)
            if node.right:
                bfs(node.right, depth + 1)

        if root:
            bfs(root, 0)
        return working


