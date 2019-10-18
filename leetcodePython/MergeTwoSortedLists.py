'''
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-two-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 迭代
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        pre_res:ListNode = ListNode(-1);
        cp = pre_res
        while (l1 and l2):
            if (l1.val < l2.val):
                cp.next = l2
                l1 = l1.next
            else:
                cp.next = l1
                l2 = l2.next
            cp = cp.next

        cp.next = l1 if l1 else l2
        return pre_res.next