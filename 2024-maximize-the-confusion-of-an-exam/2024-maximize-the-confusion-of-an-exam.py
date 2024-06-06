class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        def checkSize(size):
            
            total_t = total_f = 0
            i = 0
            while i < size:
                if answerKey[i] == "T":
                    total_t += 1
                else:
                    total_f += 1
                i += 1
                
            if min(total_t, total_f) <= k:
                return True
            l = 0
            for r in range(size, len(answerKey)):
                if answerKey[r] == "T":
                    total_t += 1
                else:
                    total_f += 1
                
                if answerKey[l] == "T":
                    total_t -= 1
                else:
                    total_f -= 1
                
                l += 1
                if min(total_t, total_f) <= k:
                    return True
            
            return False
        
        l = 1
        r = len(answerKey)
        best_ans = 1
        while l <= r:
            mid = (l + r) // 2
            if checkSize(mid):
                l = mid + 1
                best_ans = max(best_ans, mid)
            else:
                r = mid - 1
        
        return best_ans