class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        
        if len(nums1) > len(nums2):
            A, B = nums2, nums1
            
        total = len(nums1) + len(nums2)
        partition_length = total // 2
        
        l = 0
        r = len(A) - 1
        
        while True:
            Amid = (l + r) // 2
            Bmid = partition_length - (Amid + 1) - 1
            
            Aleft = A[Amid] if Amid > -1 else float('-inf')
            Aright = A[Amid + 1] if (Amid + 1) < len(A) else float('inf')
            Bleft = B[Bmid] if Bmid > -1 else float('-inf')
            Bright = B[Bmid + 1] if (Bmid + 1) < len(B) else float('inf')
            
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = Amid - 1
            else:
                l = Amid + 1