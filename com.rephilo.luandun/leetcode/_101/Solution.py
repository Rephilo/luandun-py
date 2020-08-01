from datastructure import TreeNode


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        """
        递归方式
        :param root:
        :return:
        """
        return self.isMirror(root, root)

    def isMirror(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if q and p:
            if p.val == q.val:
                return self.isMirror(p.right, q.left) and self.isMirror(p.left, q.right)
            return False
