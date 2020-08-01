from datastructure import TreeNode


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """
        递归方式
        :param p:
        :param q:
        :return:
        """
        if not p and not q:
            return True
        if q and p:
            if p.val == q.val:
                return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
        return False
