class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        num = [1]
        if rowIndex == 0:
            return num
        prev = num
        for _ in range(rowIndex): 
            temp = [0] + prev +[0]
            new_row=[]
            for j in range(len(prev)+1):
                new_row.append(temp[j] + temp[j+1])
            prev = new_row
        return prev