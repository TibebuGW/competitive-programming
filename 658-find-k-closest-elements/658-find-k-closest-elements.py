class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        r = len(arr)-1
        best = -1
        while l <= r:
            mid = (l+r)//2
            if x > arr[mid]:
                l = mid+1
            elif x < arr[mid]:
                r = mid-1
            else:
                best = mid
                r = mid-1
        # print(arr[l], arr[r])
        if best == -1:
            if r < 0:
                best = 0
                left = right = best
            elif l > len(arr)-1:
                best = len(arr)-1
                left = right = best
            else:
                l, r = r, l
                temp = l if abs(x-arr[l]) <= abs(x-arr[r]) else r
                left = temp
                right = temp
        else:
            left = right = best
        
        # print(best)
        
        count = 1
        while count < k:
            if 0<=left-1 and right+1<=len(arr)-1:
                if x-arr[left-1] <= arr[right+1]-x:
                    left -= 1
                else:
                    # print('1')
                    right += 1
            elif 0<left-1:
                # print('2')
                left -= 1
            elif right+1<len(arr)-1:
                # print('3')
                right += 1
            else:
                return arr
            
            # print("count",count, left, right)
            count += 1
        # print()
        return arr[left:right+1]