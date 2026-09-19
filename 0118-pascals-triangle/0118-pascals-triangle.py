class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        nums=[[1]]
        for i in range (numRows-1):
            new_row = []
            temp= [0] +nums[-1] +[0]
            for j in range(len(nums[-1])+1):
                new_row.append(temp[j]+temp[j+1])
            nums.append(new_row)
        return nums