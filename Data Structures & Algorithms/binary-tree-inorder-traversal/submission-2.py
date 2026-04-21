# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(node: Optional[TreeNode], output: list[int]) -> None:
            if node is None:
                return
            
            dfs(node.left, output)
            output.append(node.val)
            dfs(node.right, output)
        
        dfs(root, res)
        return res