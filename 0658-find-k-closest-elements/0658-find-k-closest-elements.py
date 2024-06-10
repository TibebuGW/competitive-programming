class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        r = len(arr) - 1
        best = (l + r) // 2
        
        while l <= r:
            mid = (l + r) // 2
            if abs(arr[mid] - x) < abs(arr[best] - x):
                best = mid
            elif abs(arr[mid] - x) == abs(arr[best] - x):
                best = min(best, mid)
                
            if arr[mid] == x:
                break
            elif x < arr[mid]:
                r = mid - 1
            else:
                l = mid + 1
                
        ans = [arr[best]]
        l = best - 1
        r = best + 1
        k -= 1
        while k:
            if l >= 0 and r < len(arr):
                if abs(x - arr[l]) <= abs(x - arr[r]):
                    ans.append(arr[l])
                    l -= 1
                else:
                    ans.append(arr[r])
                    r += 1
            elif l >= 0:
                ans.append(arr[l])
                l -= 1
            elif r < len(arr):
                ans.append(arr[r])
                r += 1
            
            k -= 1
        
        return sorted(ans)