class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        if a == 1:
            return 1
        result = 1
        b = [str(b[i]) for i in range(len(b))]
        exp = int("".join(b))
        base = a%1337
        while exp > 0:
            if exp%2 == 1:
                result = (result*base)%1337
            exp >>= 1
            base = (base**2)%1337
        return result
        