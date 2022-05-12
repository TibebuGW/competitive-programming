class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        sorted_str = sorted(timePoints)
        mmin = float('inf')
        # print(sorted_str)
        
        for i in range(1, len(timePoints)):
            time1 = sorted_str[i-1].split(":")
            time2 = sorted_str[i].split(":")
            # print(time1)
            # print(time2)
            result = (int(time2[0])-int(time1[0]))*60 + (int(time2[1])-int(time1[1]))
            # print(result)
            if result < mmin:
                mmin = result
        
        time1 = sorted_str[0].split(":")
        time2 = sorted_str[-1].split(":")
        # print((int(time1[0])+23)-int(time2[0]))
        result = ((int(time1[0])+23)-int(time2[0]))*60 + ((int(time1[1])+60)-int(time2[1]))
        # print(result)
        if result < mmin:
            mmin = result
        
        return mmin
            