class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        count = Counter(nums1)
        result = []
        for num in nums2 :
            if count[num] > 0:
                result.append(num)
                count[num] -= 1
            
        return result
        
        