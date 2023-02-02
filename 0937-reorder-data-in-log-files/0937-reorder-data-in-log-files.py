class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits = []
        letters = []
        
        for log in logs:
            c = 0
            while log[c] != " ":
                c += 1
            temp = [log[:c], log[c + 1:]]
            digit = False
            for char in temp[1]:
                if char.isdigit():
                    digit = True
                    break
            
            if digit:
                digits.append(temp)
            else:
                letters.append([temp[1], temp[0]])
        
        ans = []
        letters.sort()
        for letter in letters:
            temp = [letter[1], letter[0]]
            ans.append(" ".join(temp))
        
        for digit in digits:
            ans.append(" ".join(digit))
        
        return ans