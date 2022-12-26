class Solution:
    def findMin(self, nums: List[int]) -> int:

        def binarySearch(l = 0, r = len(nums) - 1):
            best = float('inf')
            cur = float('inf')

            if l == r:
                return nums[r]

            while l <= r:
                mid = (l + r)//2

                if nums[mid] > nums[r]:
                    l = mid + 1
                elif nums[mid] < nums[l]:
                    r = mid - 1
                else:
                    cur = min(binarySearch(l, mid), binarySearch(mid + 1, r))
                    return min(cur, best)

                best = min(best, nums[mid])

            return best

        return binarySearch()
