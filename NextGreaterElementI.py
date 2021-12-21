class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        stack = [nums2[0]]
     
        
        for i in range(1, len(nums2), 1):
            while len(stack) != 0 and stack[-1] < nums2[i]:
                d[stack.pop()] = nums2[i]
                
            stack.append(nums2[i])
            
        for i in range(0, len(stack), 1):
            d[stack[i]] = -1
            
        for i in range(0, len(nums1), 1):
            nums1[i] = d[nums1[i]]
            
        return nums1
