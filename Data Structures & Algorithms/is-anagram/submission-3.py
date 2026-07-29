class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        lst_s = sorted(list(s))
        lst_t = sorted(list(t))

        for i in range(len(lst_s)):
            if lst_s[i] != lst_t[i]:
                return False

        return True