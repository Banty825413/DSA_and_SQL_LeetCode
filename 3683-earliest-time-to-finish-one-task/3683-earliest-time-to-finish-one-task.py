class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
       result = float('inf')
       for item in tasks :
            result = min(item[0] +item[1],result)
       return result