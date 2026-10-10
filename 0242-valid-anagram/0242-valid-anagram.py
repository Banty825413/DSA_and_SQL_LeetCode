class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        map={}

        for ch in s:
            map[ch] = map.get(ch,0)+1
        for ch in t :
            if ch not in map or map[ch] ==0:
                return False
            else:
                map[ch] -=1 
        return True