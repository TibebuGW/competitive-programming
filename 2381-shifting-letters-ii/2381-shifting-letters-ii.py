from itertools import accumulate
class Solution:
    def shifter(self, char, val):
        if val > 0:
            val %= 26
            if ord(char)+val <= 122:
                new_char = chr(ord(char)+val)
            else:
                new_char = chr(96+(val-(122-ord(char))))
        else:
            val = -val%26
            if ord(char)-val >= 97:
                new_char = chr(ord(char)-val)
            else:
                new_char = chr(123-(val-(ord(char)-97)))
        
        return new_char
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        shift_array = [0]*(len(s)+1)
        for start, end, direction in shifts:
            if direction:
                shift_array[start] += 1
                shift_array[end+1] -= 1
            else:
                shift_array[start] -= 1
                shift_array[end+1] += 1
        
        for i in range(1, len(shift_array)):
            shift_array[i] += shift_array[i-1]
        
        shift_array.pop()
        ans = []
        for idx, char in enumerate(s):
            ans.append(self.shifter(char, shift_array[idx]))
        return "".join(ans)