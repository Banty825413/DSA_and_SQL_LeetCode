class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word_list = s.split()
        if len(word_list)  != len(pattern): return False 
        map ={}
        for a , b in zip(pattern , word_list):
            if a not in map:
                if b not in map.values():
                    map[a]  = b
                else:
                    return False
            elif map[a] != b :
                return False
        return True