class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        last = -1
        arr = list(palindrome)

        for i, char in enumerate(arr):
            if char == "a":
                arr[i] = "b"
                if arr != arr[::-1]:
                    last = i
                arr[i] = "a"
            else:
                arr[i] = "a"
                if arr == arr[::-1]:
                    arr[i] = char
                else:
                    return "".join(arr)
        if last != -1:
            arr[last] = "b"
            return "".join(arr)
        else:
            return ""