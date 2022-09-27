class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        flag = True
        d = {}
        dominoes = list(dominoes)
        while flag:
            i = 0
            flag = False
            while i < len(dominoes):
                if dominoes[i] == ".":
                    if i != 0:
                        left = dominoes[i-1]
                    else:
                        left = None
                    
                    if i != len(dominoes)-1:
                        right = dominoes[i+1]
                    else:
                        right = None
                    
                    
                    if left != "R" and right == "L":
                        d[i] = "L"
                    elif right != "L" and left == "R":
                        d[i] = "R"
        
                i+=1
            if len(d):
                flag = True
                for index, char in enumerate(dominoes):
                    if index in d:
                        dominoes[index] = d[index]
                d = {}
        
        
        # print(d)
        return "".join(dominoes)