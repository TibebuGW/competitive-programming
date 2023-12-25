class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        visited = defaultdict(int)
        
        i = 0
        for j in range(len(nums)):
            if visited[nums[j]] == 0:
                nums[i] = nums[j]
                i += 1
            visited[nums[j]] += 1
        
        return len(visited)
        