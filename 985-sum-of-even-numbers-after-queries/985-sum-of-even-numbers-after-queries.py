class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        total = sum([val for val in nums if val%2 == 0])
        ans = []
        for value, index in queries:
            if nums[index]%2 == 1:
                nums[index]+=value
                if (nums[index])%2 == 0:
                    total += nums[index]
                ans.append(total)
            else:
                total -= nums[index]
                nums[index] += value
                if nums[index]%2 == 0:
                    total += nums[index]
                ans.append(total)
                
        return ans