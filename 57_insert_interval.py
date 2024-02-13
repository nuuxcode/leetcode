class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        for i, inter in enumerate(intervals):
            end = inter[1]
            start = inter[0]
            if newInterval[0] > end:
                result.append(inter)
            elif newInterval[1] < start:
                result.append(newInterval)
                return result+intervals[i:]
            else:
                new_min=min(start,newInterval[0])
                new_max=max(end,newInterval[1])
                newInterval=[new_min,new_max]
        result.append(newInterval)
        return result
