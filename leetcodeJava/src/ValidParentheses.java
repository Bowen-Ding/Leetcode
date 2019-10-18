/*
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
 */

import java.util.HashMap;
import java.util.Stack;

public class ValidParentheses {
    /*
    思路
    a.用一个map来存储括号映射关系, 遍历输入字符串, 用栈来保存正括号, 当遇到反括号时, 和栈顶元素(通过map)进行匹配, 若不能匹配直接返回false, 可以匹配则继续遍历
    b.当遍历完成后, 检测栈中是否还有未匹配完的元素, 返回结果
    */
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        HashMap<Character,Character> m = new HashMap<Character, Character>();
        m.put(')','(');
        m.put('}','{');
        m.put(']','[');
        for (int i = 0; i < s.length(); i++) {
            char cur = s.charAt(i);
            if (m.containsKey(cur)) {
                char top = stack.isEmpty() ? '#':stack.pop();
                if (top != m.get(cur)) return false;
            }
            else {
                stack.push(cur);
            }
        }
        return stack.isEmpty();
    }
}
