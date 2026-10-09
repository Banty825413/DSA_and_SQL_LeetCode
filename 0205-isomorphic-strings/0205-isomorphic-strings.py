class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map = {}
        for key , val in zip(s,t):
            if key not in map:
                if val not in map.values():
                    map[key] = val
                else:
                    return False
            elif(map[key] != val ):
                return False

        return True