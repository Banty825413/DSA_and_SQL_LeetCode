"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        max_child = 0 
        if not root :
            return 0
        for child in root.children :
            max_child = max(max_child , self.maxDepth(child))
        
        return 1 + max_child