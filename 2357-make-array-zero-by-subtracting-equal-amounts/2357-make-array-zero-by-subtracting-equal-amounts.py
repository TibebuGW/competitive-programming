class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        s = set()
        for num in nums:
            if num and num not in s:
                count += 1
                s.add(num)
        return count