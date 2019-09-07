package LC_DynamicProgramming;

/*
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
 */
public class LongestPalindromicSubstring {
    //中心扩展法
    public String longestPalindrome(String s) {
        if (s.length() <= 1) {
            return s;
        }
        int start = 0;
        int end = 0;
        for (int i = 0;i < s.length();i++) {
            int len1 = expandAroundCenter(s,i,i);
            int len2 = expandAroundCenter(s,i,i + 1);
            int len = Math.max(len1,len2);
            if (len > (end - start + 1)) {
                start = i - (len - 1)/2;
                end = i + (len)/2;
            }
        }
        return s.substring(start,end + 1);
    }

    public int expandAroundCenter(String s,int left,int right) {
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }
        return right - left - 1;
    }

    //动态规划
    public String longestPalindromeDP(String s) {
        if (s.length() <= 1) {
            return  s;
        }
        int length = s.length();
        boolean[][] dp = new boolean[length][length];
        int maxLen = 0;
        String maxPal = "";
        for (int end = 1 ; end < length;end++) {
            for (int start = 0;start <= end;start++ ) {
                dp[start][end] = (end - start <= 2 || dp[start + 1][end - 1]) && s.charAt(start) == s.charAt(end);
                int len = end - start + 1;
                if (dp[start][end] && len > maxLen) {
                    maxLen = len;
                    maxPal = s.substring(start,end + 1);
                }
            }
        }
        return  maxPal;
    }
}
