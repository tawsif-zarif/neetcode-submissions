class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = list(s)
        palindrome = []
        for c in s:
            if c.isalnum():
                palindrome.append(c)
            else:
                continue

        palindrome = [x.lower() for x in palindrome]

        if palindrome == list(reversed(palindrome)):
            return True
        else:
            return False
        