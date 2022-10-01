class Solution:
    def numDecodings(self, s: str) -> int:
        s = list(s)
        dp = [0]*(len(s)) + [1,0]
        
        j = len(s)-1
        
        while j >= 0:
            first_comp = dp[j+1]
            second_comp = dp[j+2]
            if s[j] == "0":
                if j >= 1 and s[j-1] == "1" or s[j-1] == "2":
                    second_comp = 0
                    dp[j-1] = first_comp
                    s[j-1] = "-1"
                    j -= 1
                else:
                    # print(j, s[j-1])
                    return 0
            elif s[j] == "1":
                if j < len(s)-1:
                    num = int(s[j+1])
                    if num < 1 or num > 9:
                        second_comp = 0
            elif s[j] == "2":
                if j < len(s)-1:
                    num = int(s[j+1])
                    if num < 1 or num > 6:
                        second_comp = 0
            else:
                second_comp = 0
            
            dp[j] = first_comp + second_comp
            
            j -= 1 
        # print(s)
        # print(dp)
        return dp[0]