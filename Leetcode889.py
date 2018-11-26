class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        if not pre:
            return
        root = TreeNode(pre[0])
        pre, post = pre[1:], post[:-1]
        if not pre:
            return root
        i = post.index(pre[0])
        root.left = self.constructFromPrePost(pre[:i + 1], post[:i + 1])
        root.right = self.constructFromPrePost(pre[i + 1:], post[i + 1:])
        return root


test_pre = [1, 2, 4, 5, 3, 6, 7]
test_post = [4, 5, 2, 6, 7, 3, 1]
S = Solution()
x = S.constructFromPrePost(pre=test_pre, post=test_post)
