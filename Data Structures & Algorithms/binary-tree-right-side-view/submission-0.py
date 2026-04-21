# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rightmost = []
        def bfs(node: Optional[TreeNode], depth: int) -> None:
            if node is None:
                return
            if depth >= len(rightmost):
                rightmost.append(node.val)
            else:
                rightmost[depth] = node.val
            bfs(node.left, depth + 1)
            bfs(node.right, depth + 1)
        bfs(root, 0)
        return rightmost