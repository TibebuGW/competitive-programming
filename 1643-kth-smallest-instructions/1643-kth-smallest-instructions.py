from math import *
class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        n = destination[0]
        m = destination[1]
        limit = factorial(n+m)//(factorial(n)*factorial(m))

        def rec(path = "", h_count = m, v_count = n, l = 1, r = limit):
            if h_count == v_count == 0:
                return path

            boundary = 0
            if h_count:
                boundary = l + (factorial(h_count + v_count - 1)//(factorial(v_count)*factorial(h_count-1))) - 1
            else:
                boundary = r - (factorial(h_count + v_count - 1)//(factorial(v_count-1)*factorial(h_count)))
            if l <= k <= boundary:
                string = path + "H"
                return rec(string, h_count-1, v_count, l, boundary)
            else:
                string = path + "V"
                return rec(string, h_count, v_count-1, boundary+1, r)



        return rec()

