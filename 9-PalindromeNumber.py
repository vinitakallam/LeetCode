# Problem: Given an integer x, return true if x is a  palindrome, and false otherwise.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        numstring = str(x)
        halfway = len(numstring) // 2
        for i in range(halfway):
            if numstring[i] != numstring[len(numstring) - 1 - i]:
                return False
        return True
    