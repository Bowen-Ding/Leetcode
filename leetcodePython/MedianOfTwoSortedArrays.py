'''
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
'''
class Solution:
    def findMedianSortedArrays(self, a:list, b:list) -> float:
        l1 = len(a)
        l2 = len(b)
        # 调整数组a、b,使得较长的数组为a,较短的为b
        if (l1 > l2):
            a,b,l1,l2 = b,a,l2,l1

        # mid取值时先加1再除以2,这样当长度和为奇数时,中位数为左边的最大值
        iMin,iMax,mid = 0,l1,(l1 + l2 + 1)//2
        while iMin <= iMax:
            i = (iMin + iMax)//2
            j = mid - i;

            # i太小,需要右移
            if (i < iMax and a[i] < b[j-1]):
                iMin += 1
            # i太大,需要左移
            elif (i > iMin and a[i-1] > b[j]):
                iMax -= 1;
            # i范围合适,可以找中位数了
            else:
                if i == 0:
                    maxLeft = b[j-1]
                elif j == 0:
                    maxLeft = a[i-1]
                else:
                    maxLeft = max(a[i-1],b[j-1])

                if (l1 + l2)%2 == 1:
                    return maxLeft

                if i == l1:
                    minRight = b[j]
                elif j == l2:
                    minRight = a[i]
                else:
                    minRight = min(a[i],b[j])

                return (maxLeft + minRight)/2.0

        return 0.0

str = 'abc'
str.split("ass")