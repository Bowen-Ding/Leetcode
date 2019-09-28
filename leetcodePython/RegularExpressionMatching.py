'''
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

说明:

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "a*"
输出: true
解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
示例 3:

输入:
s = "ab"
p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
示例 4:

输入:
s = "aab"
p = "c*a*b"
输出: true
解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
示例 5:

输入:
s = "mississippi"
p = "mis*is*p*."
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/regular-expression-matching
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    #解法 回溯法: 运用递归从第一个字符开始逐个判断
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        firstMatch = bool(s) and p[0] in {s[0],'.'}

        if len(p) >= 2 and p[1] == '*':
            return (firstMatch and self.isMatch(s[1:],p)) or (self.isMatch(s,p[2:]))
        else:
            return firstMatch and self.isMatch(s[1:],p[1:])

    #解法 动态规划: memo保存 s[i:] 与 p[j:] 的匹配结果
    def isMatch2(self, s: str, p: str) -> bool:
        if not p:
            return not s
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[-1][-1] = True

        #从后往前匹配
        for i in range(len(s),-1,-1):
            for j in range(len(p) - 1,-1,-1):
                firstMatch = i < len(s) and p[j] in {s[i],'.'}
                #当前j后面跟'*'时,可以匹配的条件: dp[i][j+2]可以匹配,或者 当前位置i 和 j匹配 同时dp[i+1][j]可以匹配.
                # 这里注意一点: dp[i+1][j+2]为真 -> dp[i+1][j]为真,反之不一定成立,因为可能j匹配多次,所以直接确定dp[i+1][j]
                #当j后面是其它字符时,dp[i][j]为真必须满足: 当前i和j匹配,并且i和j 的前一位置也匹配
                if j + 1 < len(p) and p[j + 1] == '*':
                    dp[i][j] = dp[i][j+2] or firstMatch and dp[i+1][j]
                else:
                    # 这里and的两个条件不可交换顺序,因为当最后一位是'*'时,先判断dp[i+1][j+1]会出现错误:out of list index
                    dp[i][j] = firstMatch and dp[i+1][j+1]

        return dp[0][0]

Solution.isMatch2(Solution,'asdsad','as*d*s*a*d*')