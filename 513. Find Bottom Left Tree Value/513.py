# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        mxlevel = -1
        mxval = None

        def dfs(root, level):
            nonlocal mxlevel
            nonlocal mxval
            if root is None:
                return
            if level > mxlevel:
                mxlevel = level
                mxval = root.val
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)

        dfs(root, 0)
        return mxval


if __name__ == '__main__':
    root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(3)
    # root.left.left = TreeNode(4)
    # root.right.left = TreeNode(5)
    # root.right.right = TreeNode(6)
    # root.right.left.left = TreeNode(7)
    sol = Solution()
    print(sol.findBottomLeftValue(root))
