class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        [l, r] = [0, len(s) - 1]
        while l < r:
            while l < r and not self.checkAlphaNum(s[l]):
                l += 1
            while l < r and not self.checkAlphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
    
    def checkAlphaNum(self, char_):
        return (ord("A") <= ord(char_) <= ord("Z") or ord("a") <= ord(char_) <= ord("z") or ord("0") <= ord(char_) <= ord("9"))