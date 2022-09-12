class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = 0
        highest = 0
        l = 0
        r = len(tokens)-1
        tokens.sort()
        while l <= r:
            if tokens[l] <= power:
                power -= tokens[l]
                score += 1
                l += 1
                highest = max(score, highest)
            else:
                if score:
                    power += tokens[r]
                    score -= 1
                r -= 1
                
        
        return highest
                