class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
        for n in digits:
            num += str(n)
        num = str(int(num)+1)
        return [char for char in num]