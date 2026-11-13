# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode | None) -> bool:
        self.value = root.val

        def bst(node):
            if  node is None :
                return True
            
            
            if node.val != self.value:
                return False
            
            return bst(node.left) and  bst(node.right)
        return bst(root)
                
            