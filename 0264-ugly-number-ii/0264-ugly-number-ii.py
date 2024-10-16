class Solution:
    def nthUglyNumber(self, n: int) -> int:
        i2, i3, i5 = 0, 0, 0
        m2, m3, m5 = 2, 3, 5
        arr = [1]
        
        while len(arr) < n:
            next_num = min(m2, m3, m5)
            if arr[-1] != next_num:
                arr.append(next_num)
            
            if next_num == m2:
                i2 += 1
                m2 = 2 * arr[i2]
            elif next_num == m3:
                i3 += 1
                m3 = 3 * arr[i3]
            else:
                i5 += 1
                m5 = 5 * arr[i5]
        
        return arr[-1]