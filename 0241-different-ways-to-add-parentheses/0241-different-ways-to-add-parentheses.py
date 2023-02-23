class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def evaluate(num1, num2, op):
            if op == "+":
                return num1 + num2
            elif op == "-":
                return num1 - num2
            else:
                return num1*num2
            
        exp_arr = []
        num = 0
        for char in expression:
            if char.isdigit():
                num = num * 10 + int(char)
            else:
                exp_arr.append(num)
                num = 0
                exp_arr.append(char)
        
        exp_arr.append(num)
        
        @lru_cache(None)
        def dp(l = 0, r = len(exp_arr) - 1):
            if l == r:
                return [exp_arr[l]]
            
            ans = []
            for i in range(l + 1, r, 2):
                left_ans = dp(l, i - 1)
                right_ans = dp(i + 1, r)
                
                for num1 in left_ans:
                    for num2 in right_ans:
                        ans.append(evaluate(num1, num2, exp_arr[i]))
            
            return ans
        
        return dp()