class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        
        
        nums.sort(reverse = True)
        result =[]
        result.append(nums[0])
        prev = nums[0]
        for i in range(1,len(nums)):
                if len(result) == k:
                    break
                if nums[i]  != prev:
                    result.append(nums[i])
                    prev = nums[i]
                
        return result
            