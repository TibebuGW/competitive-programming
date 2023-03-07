class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        mask = (1 << n) - 1
        
        ans = [[]]
        
        while mask:
            cur = []
            for i in range(n):
                if mask & (1 << i):
                    cur.append(nums[i])
            mask -= 1
            ans.append(cur)
        
        return ans