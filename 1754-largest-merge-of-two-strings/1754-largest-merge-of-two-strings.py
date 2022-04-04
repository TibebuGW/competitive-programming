class Solution:
    def largestMerge(self, list1: str, list2: str) -> str:
        n = len(list1)
        m = len(list2)
        pointer1 = pointer2 = 0
        result = []
        while pointer1 < n and pointer2 < m:
            if list1[pointer1] > list2[pointer2]:
                result.append(list1[pointer1])
                pointer1 += 1
            elif list2[pointer2] > list1[pointer1]:
                result.append(list2[pointer2])
                pointer2 += 1
            else:
                if list1[pointer1+1:] >= list2[pointer2+1:]:
                    result.append(list1[pointer1])
                    pointer1 += 1
                elif list1[pointer1+1:] < list2[pointer2+1:]:
                    result.append(list2[pointer2])
                    pointer2 += 1
        
        if pointer1 < n and pointer2 == m:
            result.append("".join(list1[pointer1:]))
        if pointer2 < m and pointer1 == n:
            result.append("".join(list2[pointer2:]))
        

        return "".join(result)
                    
                