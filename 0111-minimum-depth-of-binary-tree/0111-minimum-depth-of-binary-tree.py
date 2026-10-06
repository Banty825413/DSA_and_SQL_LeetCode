# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode | None) -> int:

        
        
            deep = 0
            q = deque([root])
            if not root : return 0

            while(q):
                deep += 1
                for _ in range (len(q)):
                    temp = q.popleft()

                    if not temp.left and not temp.right : return deep

                    if temp.left :  q.append(temp.left)

                    if temp.right : q.append(temp.right)
            return deep    
        

            

           

        