class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        def recursion(lst, index):
            if index == 0:
                if lst[index].isnumeric():
                    return [lst[index]]
                else:
                    return [lst[index], lst[index].upper()] if lst[index].islower() else [lst[index], lst[index].lower()]
            array_to_return = []
            arr = recursion(lst, index-1)
            if not lst[index].isnumeric():
                for string in arr:
                    temp = list(string)
                    array_to_return.append("".join(temp+[lst[index]]))
                    if lst[index].isupper():
                        array_to_return.append("".join(temp+[lst[index].lower()]))
                    else:
                        array_to_return.append("".join(temp+[lst[index].upper()]))
            else:
                for string in arr:
                    temp = list(string)
                    array_to_return.append("".join(temp+[lst[index]]))
            
            return array_to_return
        lst = list(s)
        return recursion(lst, len(s)-1)