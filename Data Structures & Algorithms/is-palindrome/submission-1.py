class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_list = [char.lower() for char in s if char.isalnum()]
        return clean_list == clean_list[::-1]