class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = Counter(nums)
        result = []
        # print(d)
        for key, value in d.items():
            if value > len(nums)//3:
                result.append(key)
                
        return result