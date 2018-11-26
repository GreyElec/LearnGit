class Solution:
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if not root:
            return 0
        return root.val + self.rangeSumBST(root.left,
                                           L,
                                           R) + self.rangeSumBST(root.right,
                                                                 L,
                                                                 R) if L <= root.val <= R else self.rangeSumBST(root.left,
                                                                                                                L,
                                                                                                                R) + self.rangeSumBST(root.right,
                                                                                                                                      L,
                                                                                                                                      R)
