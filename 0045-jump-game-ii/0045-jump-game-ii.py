class Solution:
    def jump(self, nums: List[int]) -> int:
        possible_indices = deque([[len(nums) - 1, 0]])
        
        for i in range(len(nums) - 2, -1, -1):
            j = 0
            max_reach = i + nums[i]
            cur_min = float('inf')
            while j < len(possible_indices) and max_reach >= possible_indices[j][0]:
                cur_min = min(cur_min, possible_indices[j][1])
                j += 1
            if cur_min < float('inf'):
                possible_indices.appendleft([i, cur_min + 1])
        
        return possible_indices[0][1]