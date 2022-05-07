class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        smallest = min(strs, key=len)
        # idx = strs.index(smallest)
        for i in range(len(smallest)):
            for j in range(1, len(strs)):
                if strs[j][:i+1] != strs[j-1][:i+1]:
                    return result
            result = strs[0][:i+1]
        
        return result