'''
Date: 2022-04-11 20:14:04
LastEditors: r7000p
LastEditTime: 2022-04-21 20:32:24
FilePath: \Daily\daily-python\2.py
'''
# git test
# compare
arr = [[1,4],[0,2],[3,5]]
# print(arr)

def merge(intervals):
    intervals.sort()
    i = 0
    while i < len(intervals) - 1:
        if intervals[i+1][0] < intervals[i][1]:
            if intervals[i+1][1] < intervals[i][1]:
                del intervals[i+1]
            else:
                intervals[i][1] = intervals[i+1][1]
                del intervals[i+1]
        else:
            i += 1
    print(intervals)

merge(arr)