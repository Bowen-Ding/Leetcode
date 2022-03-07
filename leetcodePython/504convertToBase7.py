'''
504. 七进制数
给定一个整数 num，将其转化为 7 进制，并以字符串形式输出。

 

示例 1:

输入: num = 100
输出: "202"
示例 2:

输入: num = -7
输出: "-10"
 

提示：

-10^7 <= num <= 10^7
'''

class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        if num < 0:
            num = 0 - num
            flag = 1
        else:
            flag = 0
        ans = ''
        while num > 0:
            ch = num % 7
            ans = str(ch) + ans
            num //= 7
        
        ans = '-' + ans if flag == 1 else ans
        return ans