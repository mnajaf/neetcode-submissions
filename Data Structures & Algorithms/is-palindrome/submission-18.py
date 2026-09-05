class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = ""
        for char in s:
            if char.isalnum():
                newstr = newstr + char.lower()

        return newstr == newstr[::-1]

        