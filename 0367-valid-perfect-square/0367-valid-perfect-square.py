class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        left = 0 
        right = num //2
        while left <= right :
            mid = left + (right - left )//2
            temp = mid *mid
            if temp == num:
                return True
            elif temp < num:
                left = mid+1
            else:
                right = mid-1
        return False