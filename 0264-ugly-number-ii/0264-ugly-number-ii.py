class Solution:
    def nthUglyNumber(self, n: int) -> int:
        index_of_2 = index_of_3 = index_of_5 = 0
        next_multiple_2 = 2
        next_multiple_3 = 3
        next_multiple_5 = 5
        
        arr = [1]
        while len(arr) < n:
            next_value = min(next_multiple_2, next_multiple_3, next_multiple_5)
            if arr[-1] != next_value:
                arr.append(next_value)
            if next_value == next_multiple_2:
                index_of_2 += 1
                next_multiple_2 = arr[index_of_2]*2
            elif next_value == next_multiple_3:
                index_of_3 += 1
                next_multiple_3 = arr[index_of_3]*3
            else:
                index_of_5 += 1
                next_multiple_5 = arr[index_of_5]*5
        return arr[-1]