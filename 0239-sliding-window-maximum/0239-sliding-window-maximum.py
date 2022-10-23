from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue_window = deque()
        for i in range(k):
            while queue_window and nums[queue_window[-1]] < nums[i]:
                queue_window.pop()
            queue_window.append(i)
                
        arr = [nums[queue_window[0]]]
        l = 0
        for r in range(k, len(nums)):
            if queue_window[0] == l:
                queue_window.popleft()
            while queue_window and nums[queue_window[-1]] < nums[r]:
                queue_window.pop()
            queue_window.append(r)
            arr.append(nums[queue_window[0]])
            l += 1
        return arr