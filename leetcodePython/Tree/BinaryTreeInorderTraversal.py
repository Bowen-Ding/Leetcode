'''
给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]

进阶: 递归算法很简单，你可以通过迭代算法完成吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-inorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        # p作为指针
        p = root
        while p or stack:
            while p:
                stack.append(p)
                p = p.left # 左子树优先入栈
            # 获取栈顶元素
            tmp = stack.pop()
            res.append(tmp.val)
            # 没有左子树时,右子树入栈
            p = tmp.right
        
        return res

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None