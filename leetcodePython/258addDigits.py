'''
给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。返回这个结果。

 

示例 1:

输入: num = 38
输出: 2 
解释: 各位相加的过程为：
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2
由于 2 是一位数，所以返回 2。
示例 1:

输入: num = 0
输出: 0
 

提示：

0 <= num <= 2^31 - 1
'''


class Solution:
    def addDigits(self, num: int) -> int:
        ans = 0
        while num > 0:
            ans += num % 10
            num //= 10
        
        if ans >= 10:
            ans = self.addDigits(ans)
        
        return ans