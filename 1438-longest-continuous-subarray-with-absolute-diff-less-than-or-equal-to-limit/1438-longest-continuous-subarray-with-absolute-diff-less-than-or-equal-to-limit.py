class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        inc_q = deque([])
        dec_q = deque([])
        
        ans = 0
        l = 0
        for r in range(len(nums)):
            while inc_q and nums[inc_q[-1]] > nums[r]:
                inc_q.pop()
            inc_q.append(r)
            
            while dec_q and nums[dec_q[-1]] < nums[r]:
                dec_q.pop()
            dec_q.append(r)
            
            while nums[dec_q[0]] - nums[inc_q[0]] > limit:
                if dec_q[0] == l:
                    dec_q.popleft()
                if inc_q[0] == l:
                    inc_q.popleft()
                l += 1
            
            ans = max(ans, r - l + 1)
        
        return ans