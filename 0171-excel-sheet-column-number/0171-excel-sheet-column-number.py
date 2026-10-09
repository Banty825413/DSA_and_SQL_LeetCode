class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        i= 0
        while columnTitle:
            temp = columnTitle[-1]
            columnTitle = columnTitle[:-1]
            result += 26**i * (ord(temp)- 64) 
            i += 1
        return result