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
            if node is None:
                return
            if depth >= len(working):
                working.append([])
            working[depth].append(node.val)

            bfs(node.left, depth + 1)
            bfs(node.right, depth + 1)

        bfs(root, 0)
        return working


