#Given a string s, return true if it is a palindrome, otherwise return false.
#A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.
#Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            while not s[i].isalnum() and i < j:
                i += 1
            while not s[j].isalnum() and j > i:
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
