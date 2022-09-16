class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        nums1 = nums[:-1]
        nums2 = nums[1:]

        for i in range(1, len(nums1)):
            if i == 1:
                nums1[i] = max(nums1[0], nums1[1])
            else:
                nums1[i] = max(nums1[i]+nums1[i-2], nums1[i-1])

        for i in range(1, len(nums2)):
            if i == 1:
                nums2[i] = max(nums2[0], nums2[1])
            else:
                nums2[i] = max(nums2[i]+nums2[i-2], nums2[i-1])
        # print(nums1)
        # print(nums2)
        return max(nums1[-1], nums2[-1])