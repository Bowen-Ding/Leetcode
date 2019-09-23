'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    #解法1: 通过划动窗口完成,确定起点i,右边界j,加入set中,不断右移j,知道j已经在set中,得到无重复子串长度;遍历起点i,找到最长的无重复字符子串
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, m, win = len(s), 0, set()
        i, j = 0, 0
        while i < l and j < l:
            if (s[j] not in win):
                win.add(s[j])
                m = max(m, j - i + 1)
                j += 1
            else:
                win.remove(s[i])
                i += 1
        return m

    #解法2: 优化方法,当j已经在set中出现过,那么i可以直接移到j第一次出现的索引之后一位,而不是移动一格,用map存储(j,j的index)
    def lengthOfLongestSubstring2(self, s: str) -> int:
        l, m, dic = len(s), 0, {}
        i, j = 0, 0
        for j in range(l):
            if (s[j] in dic.keys()):
                i = max(i, dic[s[j]])
            dic[s[j]] = j + 1
            m = max(m, j - i + 1)
            j += 1
        return m

