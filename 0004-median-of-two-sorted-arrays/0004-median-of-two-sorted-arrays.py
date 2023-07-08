class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2
        
        total = len(A) + len(B)
        half = total//2
        
        if len(B) < len(A):
            A, B = B, A
        
        l = 0
        r = len(A) - 1
        
        while True:
            
            Amid = (l + r)//2
            Bmid = half - Amid - 2
            
            Aleft = A[Amid] if Amid >=0 else float('-inf')
            Aright = A[Amid + 1] if Amid + 1 < len(A) else float('inf')
            Bleft = B[Bmid] if Bmid >=0 else float('-inf')
            Bright = B[Bmid + 1] if Bmid + 1 < len(B) else float('inf')
            
            if Aleft <= Bright and Bleft <= Aright:
                if total%2:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright))/2
            elif Aleft > Bright:
                r = Amid - 1
            else:
                l = Amid + 1