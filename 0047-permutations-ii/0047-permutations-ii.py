class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        counter = Counter(nums)
        
        def backtrack():
            if len(path) == len(nums):
                ans.append(path[::])
                return
            
            for num in counter:
                if counter[num]:
                    counter[num] -= 1
                    path.append(num)
                    backtrack()
                    path.pop()
                    counter[num] += 1
        
        backtrack()
        return ans