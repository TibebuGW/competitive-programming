class Solution:
    def isPalindrome(self, x: int) -> bool:
        # print(list(str(x)))
        return str(x)[::-1] == str(x) 