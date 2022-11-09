class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        # if two arrays A and B have the same mean, then the array A+B (A and B together) will also have the same mean
        # so all we have to do to prove that an array ARR can be split into two with equal means, is to prove that one split of the array ARR has the same mean as ARR
        # to do that we can check every possible length between 1 and len(ARR)-1 inclusive and see if we can form a sum where the division between the sum and the length is equal to mean(ARR).
        # but that means a 2^30 time-complexity at worst. so instead of checking every possible mean for every possible length, we can rearrrage the formula sumA/lenA == total/N to sumA == total*lenA/N. this means the sum of a subset of the original array needs to be a whole number (integer). so for different possible subset lengths(lenA), we can rule out some lengths which don't have a whole number sumA. as a further optimization we only need to check for lengths between 1 and N//2 inclusive because if we go beyond this point without finding a possible sumA//lenA == total//N there's no answer beyond that point as we are just checking both ways which is unnecessary.
        
        N = len(nums)
        total = sum(nums)
        @lru_cache(None)
        def dp(sumA, lenA, index):
            if sumA == lenA == 0:
                return True
            if sumA < 0 or lenA < 0 or index == N:
                return False
            
            return dp(sumA-nums[index], lenA-1, index+1) or dp(sumA, lenA, index+1)
        for lenA in range(1, (N//2)+1):
            sumA = (total*lenA)//N
            if (total*lenA)%N == 0 and dp(sumA, lenA, 0):
                return True
        
        return False