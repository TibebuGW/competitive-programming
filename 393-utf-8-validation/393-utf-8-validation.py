class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        
        def checker(arr, count):
            if count != len(arr):
                # print("here")
                return False
            for char in arr:
                if char[0] != '1' or char[1] != '0':
                    return False
            return True
        
        b = []
        
        for num in data:
            temp = (8-len(bin(num)[2:]))*'0' + bin(num)[2:]
            b.append(temp)
        
        # print(b)
        i = 0
        while i < len(b):
            if b[i][0] == '0':
                i += 1
                continue
            else:
                count = 0
                for bit in b[i]:
                    if bit == '0':
                        break
                    else:
                        count += 1
                if count == 1 or count > 4 or not checker(b[i+1:i+count], count-1):
                    return False
                i += count
        
        return True