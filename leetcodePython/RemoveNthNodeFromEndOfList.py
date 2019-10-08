'''
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 双指针start和end, 先让start移动n + 1步, 再同时移动, 直到start为空, 此时end后面一个节点就是要删除的节点;
    # 设置一个dummy在head前面是因为head可能被删除, 返回dummy.next作为结果更稳定
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        start = dummy
        end = dummy
        while n != 0:
            start = start.next
            n -= 1
        while start:
            start = start.next
            end = end.next

        end.next = end.next.next
        return dummy.next