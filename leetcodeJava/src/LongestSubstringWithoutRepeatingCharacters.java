import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

/*
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
 */
public class LongestSubstringWithoutRepeatingCharacters {
    //解法1: 通过划动窗口完成,确定起点i,右边界j,加入set中,不断右移j,知道j已经在set中,得到无重复子串长度;遍历起点i,找到最长的无重复字符子串
    public int lengthOfLongestSubstring(String s) {
        int l = s.length();
        Set<Character> set = new HashSet<>();
        int max = 0,i=0,j=0;
        while (i < l && j < l) {
            if (!set.contains(s.charAt(j))) {
                set.add(s.charAt(j++));
                max = Math.max(max,j-i);
            }
            else {
                set.remove(s.charAt(i++));
            }
        }
        return max;
    }

    //解法2: 优化方法,当j已经在set中出现过,那么i可以直接移到j第一次出现的索引之后一位,而不是移动一格,用map存储(j,j的index)
    public int lengthOfLongestSubstring2(String s) {
        int l = s.length(),max = 0;
        Map<Character,Integer> m = new HashMap<>();
        for (int i = 0,j = 0;j < l;j++) {
            if (m.containsKey(s.charAt(j))) {
                i = Math.max(m.get(s.charAt(j)),i);
            }
            max = Math.max(max,j - i + 1);
            //也可以在前面i赋值时j的index加1,最后效果都是i移到j后一位
            m.put(s.charAt(j),j + 1);
        }
        return max;
    }

    /*
    解法3: ascii码值数组代替map结构,常用数组如下:
        int [26] 用于字母 ‘a’ - ‘z’ 或 ‘A’ - ‘Z’
        int [128] 用于ASCII码
        int [256] 用于扩展ASCII码
    */
    public int lengthOfLongestSubstring3(String s) {
        int l = s.length(),max = 0;
        int[] index = new int[128];
        for (int i = 0,j = 0;j < l; j++) {
            i = Math.max(index[s.charAt(j)],i);
            max = Math.max(max,j - i + 1);
            index[s.charAt(j)] = j + 1;
        }
        return max;
    }
}
