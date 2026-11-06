# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()

        def bst(node):
            if not node :
                return False

            
            if node.val  in seen:
                return True 
            else:
                seen.add(k - node.val)

            
            return bst(node.right) or bst(node.left)
        return bst(root)
