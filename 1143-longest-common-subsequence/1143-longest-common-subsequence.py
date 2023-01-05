class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        
        # TAP DAWN
        @lru_cache(None)
        def dp(idx1 = n - 1, idx2 = m - 1):
            if idx1 == 0:
                for idx in range(idx2, -1, -1):
                    if text1[idx1] == text2[idx]:
                        return 1
                return 0
            
            if idx2 == 0:
                for idx in range(idx1, -1, -1):
                    if text1[idx] == text2[idx2]:
                        return 1
                return 0
        
            
            if text1[idx1] == text2[idx2]:
                return 1 + dp(idx1 - 1, idx2 - 1)
            
            return max(dp(idx1 - 1, idx2), dp(idx1, idx2 - 1))
        
        # return dp()
        
        # BATTAM UP
        dp = [[0 for _ in range(m)] for _ in range(n)]
        
        for idx1 in range(n):
            if text2[0] == text1[idx1]:
                if idx1 == 0:
                    dp[idx1][0] = 1
                else:
                    dp[idx1][0] = min(dp[idx1 - 1][0] + 1, 1)
            else:
                if idx1 != 0:
                    dp[idx1][0] = dp[idx1 - 1][0]
        
        for idx2 in range(m):
            if text1[0] == text2[idx2]:
                if idx2 == 0:
                    dp[0][idx2] = 1
                else:
                    dp[0][idx2] = min(dp[0][idx2 - 1] + 1, 1)
            else:
                if idx2 != 0:
                    dp[0][idx2] = dp[0][idx2 - 1]
        
        for idx1 in range(1, n):
            for idx2 in range(1, m):
                if text1[idx1] == text2[idx2]:
                    dp[idx1][idx2] = 1 + dp[idx1 - 1][idx2 - 1]
                else:
                    dp[idx1][idx2] = max(dp[idx1 - 1][idx2], dp[idx1][idx2 - 1])
        
        # print(dp)
        
        return dp[-1][-1]