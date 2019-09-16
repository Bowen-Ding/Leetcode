'''
给出一个区间的集合，请合并所有重叠的区间。

示例 1:

输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:

输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-intervals
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    #先把intervals排序,排序完毕后依次添加intervals元素,若后一元素的start>=前一元素的end,则合并
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort();
        n = len(intervals)
        if n == 0:
            return []
        result = [intervals[0]]
        for i in range(1,n):
            if intervals[i][0] <= result[-1][1]:
                result[-1][1] = max(intervals[i][1],result[-1][1])
            else:
                result.append(intervals[i])
        return result