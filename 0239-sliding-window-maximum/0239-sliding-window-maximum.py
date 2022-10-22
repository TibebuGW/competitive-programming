from sortedcontainers import SortedList
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        sorted_list = SortedList()
        for i in range(k):
            sorted_list.add(nums[i])
        
        arr = [sorted_list[-1]]
        
        l = 0
        for r in range(k, len(nums)):
            sorted_list.discard(nums[l])
            sorted_list.add(nums[r])
            arr.append(sorted_list[-1])
            l += 1
        return arr
        