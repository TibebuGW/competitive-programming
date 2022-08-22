class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n > 0:
            ans = log(n, 4)
            return ans == int(str(ans).split(".")[0])
        return False