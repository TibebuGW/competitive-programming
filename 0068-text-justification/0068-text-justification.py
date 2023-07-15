class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        
        r = 0
        
        while r < len(words):
            l = r
            total_allowable_width = maxWidth
            
            while r < len(words) and len(words[r]) <= total_allowable_width:
                total_allowable_width -= (len(words[r]) + 1)
                r += 1
                
            total_allowable_width += 1

            line = []
            if r != len(words):
                slots = r - l - 1
                if slots:
                    total_allowable_width += slots
                    spaces_to_distribute = total_allowable_width//slots
                    left_space = total_allowable_width%slots

                    for i in range(l, r):
                        line.append(words[i])
                        if i != r - 1:
                            line.append(" "*(spaces_to_distribute + int(left_space > 0)))
                            left_space -= 1
                else:
                    line.append(words[l])
                    line.append(" "*total_allowable_width)

            else:
                for i in range(l, r):
                    line.append(words[i])
                    if i != len(words) - 1:
                        line.append(" ")
                
                line.append(" "*total_allowable_width)
                
            ans.append("".join(line))
        
        return ans