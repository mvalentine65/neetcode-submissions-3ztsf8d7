# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        def recurse(node: Optional[TreeNode], total:int=0) -> bool:
            if node is None:
                return False
            print(node.val, total)
            if not node.left and not node.right:
                return total + node.val == targetSum
            return recurse(node.left, total + node.val) or recurse(node.right, total + node.val)
        return recurse(root)

            
