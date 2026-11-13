# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode | None, x: int, y: int) -> bool:
        queue = deque([root])
        
        while queue :
            found_x = found_y = False
            for _ in range(len(queue)):
                temp = queue.popleft()

                if temp.left and temp.right:

                    if{temp.left.val,temp.right.val} == {x,y}:
                        return False
                    
                for child in (temp.left ,temp.right):
                        if child:
                            if child.val == x :
                                found_x  = True
                            if child.val == y:
                                found_y = True
                            queue.append(child)
                    
            if found_x and found_y :
                return True
            if found_x or found_y :
                return False
        return False


                
