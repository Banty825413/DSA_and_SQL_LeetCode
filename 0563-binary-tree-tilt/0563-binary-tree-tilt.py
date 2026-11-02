# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        self.result = 0

        def tilt(node):

            if not node :
                return 0 
            
            left = tilt(node.left)
            right = tilt(node.right)
            self.result +=  abs(left - right)
            return node.val + left + right 
        tilt(root)
        return self.result
