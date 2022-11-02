class Solution:
    def minSteps(self, start, end, bank):
        if start == end:
            return 0
        min_ = float('inf')
        for i in range(8):
            for char in ["A","C","G","T"]:
                intermediate = list(start)
                intermediate[i] = char
                intermediate = "".join(intermediate)
                if intermediate in bank:
                    bank.remove(intermediate)
                    min_ = min(min_, self.minSteps(intermediate, end, bank))
        return min_+1
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        if start in bank:
            bank.remove(start)
        ans = self.minSteps(start, end, bank)
        return ans if ans != float('inf') else -1