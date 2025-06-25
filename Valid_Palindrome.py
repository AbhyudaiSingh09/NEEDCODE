# Given a string s, return true if it is a palindrome, otherwise return false.

# A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

# Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).



class Solution:
    def isPalindrome(self, s):
        cleaned_s = ""

        for i in s:
            if i.isalnum():
                cleaned_s += i.lower()
            
        left = 0 
        right = len(cleaned_s)-1
        while left < right:
            if cleaned_s[left] != cleaned_s[right]:
                return False
            else:
                left += 1 
                right -= 1 
        return True 
        