class Solution:
    def reverseVowels(self, s: str) -> str:
        list = set(['a','i','e','o','u','A','E','I','O','U'])
        temp =[]
        for ch in s :
            if ch in list:
                temp.append(ch)
        
        
        char = ''
        for ch in range(len(s)):

            if s[ch] in list:
                char += temp[-1]
                temp =temp[:-1]
                
            else:
                char += s[ch]
                
        return char

