# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        result = []
        def bst (root,path):
            if not root : return

            path.append(str(root.val))

            if not root.left and not root.right:
                result.append('->'.join(path))
                
            else:
                bst(root.left,path)
                bst(root.right,path)
            path.pop()

        bst(root,[])
        return result  
            

            
            
