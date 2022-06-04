class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = Counter(nums)
        # print(d)
        return max(d, key=d.get)