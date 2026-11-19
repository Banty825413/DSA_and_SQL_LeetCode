class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        
        result = float('inf')
        right = len(tasks) -1
        if right == 0:
            return tasks[0][0] + tasks[0][1]
        left = 0
        while left <= right :

            if left >= 0 :
                temp = tasks[left] 
                result = min(result , temp[0]+temp[1])
                left += 1
            
            temp = tasks[right]
            result = min(result , temp[0]+temp[1])
            right -= 1
        return result 