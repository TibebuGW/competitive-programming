class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        arr = nums[n-k:] + nums[:n-k]
        for i in range(len(nums)):
            nums[i] = arr[i]