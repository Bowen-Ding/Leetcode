import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

/*
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
 */
public class MergeIntervals {
    //将区间左端点排序,然后依次插入数组,若后一个区间的左端点大于前一个区间右端点,则这两区间可以合并
    public int[][] merge(int[][] intervals) {
        List<int[]> res = new ArrayList<>();
        if (intervals == null | intervals.length == 0)
            return  res.toArray(new int[0][]);

        Arrays.sort(intervals,new IntervalsComparator());
        int i = 0;
        while (i < intervals.length) {
            int start = intervals[i][0];
            int end = intervals[i][1];
            while (i < intervals.length - 1 && end >= intervals[i + 1][0]) {
                i++;
                end = Math.max(end,intervals[i + 1][1]);
            }
            res.add(new int[]{start,end});
            i++;
        }
        return res.toArray(new int[0][]);
    }

    private class IntervalsComparator implements Comparator<int[]> {
        @Override
        public int compare(int[] o1,int[] o2) {

            return o1[0] - o2[0];
        }
    }
}
