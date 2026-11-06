# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode | None) -> list[float]:
        if not root :
            return []
            
        result =[]
        queue = deque([root])

        while queue:
            size = len(queue)
            temp_sum = 0

            for _ in range(size):
                temp_node = queue.popleft()
                temp_sum += temp_node.val
                if temp_node.left:
                    queue.append(temp_node.left)
                if temp_node.right:
                    queue.append(temp_node.right)
            result.append(temp_sum/size)
        return result
        
            

            
            