class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        toReturn = 0
        i = len(piles)-2
        n = 0
        while n != len(piles)/3:
            print(i)
            toReturn += piles[i]
            i -= 2
            n += 1
            
        return toReturn
