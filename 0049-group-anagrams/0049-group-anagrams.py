class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        result = []
        
        for word in strs:
            temp_dict = {}
            for char in word:
                if char in temp_dict:
                    temp_dict[char] += 1
                else:
                    temp_dict[char] = 1
            ordered_dict = OrderedDict(sorted(temp_dict.items()))
            anagram = []
            for key in ordered_dict:
                anagram.append(key)
                anagram.append(str(ordered_dict[key]))
            
            anagram = "".join(anagram)
            anagrams[anagram].append(word)
        for key, val in anagrams.items():
            result.append(val)
        
        return result