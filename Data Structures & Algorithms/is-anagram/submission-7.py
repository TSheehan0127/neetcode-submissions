class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        alph = [0] * 26

        for i in s:
            alph[ord(i) - ord('a')] += 1
        
        for i in t:
            alph[ord(i) - ord('a')] -= 1
        
        for a in alph:
            if a != 0:
                return False
        return True

