# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:

        if not root : return True

        def istrue( left , right):
            if not left and not right : return True

            if not left or not right : return False

            if left.val != right.val: return False

            return istrue(left.left, right.right) and istrue(left.right, right.left)
        return istrue(root.left, root.right)