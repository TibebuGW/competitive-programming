class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split(" ")
        for index, word in enumerate(arr):
            arr[index] = word[::-1]
        
        # print(arr)
        return " ".join(arr)