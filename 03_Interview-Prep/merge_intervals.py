class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])
        final = [intervals[0]]
        for start, end in intervals[1:]:
            current_end = final[-1][1]
            if current_end >= start:
                final[-1][1] = max(current_end, end)
            else:
                final.append([start, end])
        return final
