import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        punc = s.translate(str.maketrans("", "", string.punctuation))
        punc = punc.replace(" ", "").lower()
        if punc == punc[::-1]:
            return True
        return False


        