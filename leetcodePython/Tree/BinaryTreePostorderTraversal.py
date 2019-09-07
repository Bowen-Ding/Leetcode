'''
给定一个二叉树，返回它的 后序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [3,2,1]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-postorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        list = []
        if root is None:  # 基准条件
            return []
        list += self.postorderTraversal(root.left)  # 先添加左节点
        list += self.postorderTraversal(root.right)  # 再添加右节点
        list += [root.val]  # 最后添加根节点
        return list


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None