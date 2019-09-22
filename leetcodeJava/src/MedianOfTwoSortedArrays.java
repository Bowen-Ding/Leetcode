/*
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
 */
public class MedianOfTwoSortedArrays {
    public double findMedianSortedArrays(int[] a, int[] b) {
        int l1 = a.length;
        int l2 = b.length;
        //调整数组a、b,使得较长的数组为a,较短的为b
        if (l1 > l2) {
            int[] temp = a;a = b;b = temp;
            int tmp = l1;l1 = l2;l2 = tmp;
        }
        //mid取值时先加1再除以2,这样当长度和为奇数时,中位数为左边的最大值
        int iMin = 0,iMax = l1,mid = (l1 + l2 + 1)/2;
        while (iMin <= iMax) {
            int i = (iMin + iMax)/2;
            int j = mid - i;
            //i太小,需要右移
            if (i < iMax && a[i] < b[j-1] ) {
                iMin = i + 1;
            }
            //i太大,需要左移
            else if (i > iMin && a[i-1] > b[j]) {
                iMax = i - 1;
            }
            //i范围合适,可以找中位数了
            else {
                int maxLeft = 0;
                if (i == 0) { maxLeft = b[j - 1];}
                else if (j == 0) {maxLeft = a[i-1];}
                else {maxLeft = Math.max(a[i-1],b[j-1]);}

                if ((l1 + l2)%2 == 1) return maxLeft;

                int minRight = 0;
                if (i == l1) {minRight = b[j];}
                else if (j == l2) {minRight = a[i];}
                else {minRight = Math.min(a[i],b[j]);}
                //这里必须除以2.0而不是2,不然会向下取整导致结果错误
                return (minRight + maxLeft)/2.0;
            }
        }
        return 0.0;
    }
}
