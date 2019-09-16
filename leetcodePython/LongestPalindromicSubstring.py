'''
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
'''

class Solution:
    # 中心扩展法
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 1:
            return s
        start = 0;
        end = 0;
        for i in range(len(s)):
            len1 = self.expandAroundCenter(self,s,i,i)
            len2 = self.expandAroundCenter(self,s,i,i+1)

    def expandAroundCenter(self,s,left,right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left -1

    # 动态规划法
    def longestPalindromeDP(self, s: str) -> str:
        if len(s) <= 1:
            return s
        length = len(s)
        dp = [[False for _ in range(len(s))] for _ in range(length)];
        maxLength = 0
        maxPal = ""
        for end in range(1,length):
            for start in range(end):
                dp[start][end] = (end - start <= 2 or dp[start + 1][end -1]) and s[start] == s[end]
                if (dp[start][end] and end - start + 1 > maxLength):
                    maxPal = s[start:end + 1]
                    maxLength = len(maxPal)
        return maxPal

print(Solution.longestPalindromeDP(Solution,"zzzzzzzzzzzzzz"))