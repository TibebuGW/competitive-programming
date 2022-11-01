class Solution:
    def shift(self, char, val):
        val %= 26
        
        if ord(char)+val <= 122:
            return chr(ord(char)+val)
        else:
            return chr(96+(val-(122-ord(char))))

    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        total = sum(shifts)
        new_shifts = [total]
        for i in range(len(shifts)-1):
            new_shifts.append(new_shifts[-1]-shifts[i])
        
        char_list = list(s)
        for i in range(len(s)):
            char_list[i] = self.shift(s[i], new_shifts[i])
            
        return "".join(char_list)