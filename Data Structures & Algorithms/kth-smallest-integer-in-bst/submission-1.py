# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        def dfs(node: Optional[TreeNode], i: int, element: Optional[int]) -> None:
            if node is None:
                return
            if len(stack) >= k:
                return
            
            dfs(node.left, i + 1, element)
            if len(stack) >= k:
                return
            stack.append(node.val)
            dfs(node.right, i + 1, element)

        dfs(root, i + 1, None)
        return stack[-1]