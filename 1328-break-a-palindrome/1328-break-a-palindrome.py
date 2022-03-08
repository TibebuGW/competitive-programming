class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        arr = list(palindrome)
        for i in range(len(palindrome)//2):
            if arr[i] != "a":
                arr[i] = "a"
                return "".join(arr)
        
        arr[-1] = "b"
        return "".join(arr)