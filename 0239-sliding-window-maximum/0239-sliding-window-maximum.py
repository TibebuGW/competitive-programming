class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # decreasing monotonic queue
        # the answer for any subarray of size k is the first element in the queue at that state
        # for any element you're considering to add to the queue, first remove the element outside of the window from the left of the queue
        
        # initialize a queue
        queue = deque([])
        
        # initialize an ans array
        ans = []
        
        # initialize a left pointer
        l = 0
        
        # for the first k elements, create an decreasing monotonic
        for i in range(k):
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
            
        # append the first element of the queue to the ans array
        ans.append(nums[queue[0]])
        
        # do a for loop from k - len(nums) with variable r
        # remove nums[l] if it's the first element in the queue
        # add nums[r] to the queue maintaining monotonicity
        for r in range(k, len(nums)):
            if queue[0] == l:
                queue.popleft()
            l += 1
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
            queue.append(r)
            ans.append(nums[queue[0]])
            
        # return ans
        return ans