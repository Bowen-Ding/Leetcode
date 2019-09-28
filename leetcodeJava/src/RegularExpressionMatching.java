/*
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
 */
public class RegularExpressionMatching {
    //解法 回溯法: 运用递归从第一个字符开始逐个判断
    public boolean isMatch(String s, String p) {
        if (p.isEmpty()) return s.isEmpty();
        boolean firstMatch = (!s.isEmpty() && (p.charAt(0) == s.charAt(0) || p.charAt(0) == '.'));

        if (p.length() >= 2 && p.charAt(1) == '*') {
            return (isMatch(s, p.substring(2)) || (firstMatch && isMatch(s.substring(1), p)));
        }
        else {
            return firstMatch && isMatch(s.substring(1), p.substring(1));
        }
    }

    //解法 动态规划: memo 保存 s[i:] 与 p[j:] 的匹配结果
    Result[][] memo;
    public boolean isMatch2(String s, String p) {
        memo = new Result[s.length() + 1][p.length() + 1];
        return dp(0,0,s,p);
    }

    public boolean dp(int i,int j,String s, String p) {
        if (memo[i][j] != null) return memo[i][j] == Result.True;
        boolean ans;
        if (j == p.length()) {
            ans = i == s.length();
        }
        else {
            boolean firstMatch = (i < s.length() && (s.charAt(i) == p.charAt(j) || p.charAt(j) == '.'));

            if (j + 1 < p.length() && p.charAt(j + 1) == '*') {
                ans = (dp(i,j + 2,s,p) || firstMatch && dp(i + 1,j,s,p));
            }
            else {
                ans = firstMatch && dp(i + 1,j + 1,s,p);
            }
        }

        memo[i][j] = ans ? Result.True : Result.False;
        return ans;
    }
}

enum Result {
    True, False
}