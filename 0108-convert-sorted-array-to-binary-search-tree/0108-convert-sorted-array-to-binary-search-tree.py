# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]"""
        
        if not nums :
            return None

        def getbst(arr, start ,end):
            if  start  > end :
                return None
            
            mid = (start + end) //2
            head = TreeNode(arr[mid])
            head.left = getbst(arr,start,mid-1)
            head.right = getbst(arr,mid+1, end)
            
            return head
        return getbst( nums, 0 , len(nums)-1)