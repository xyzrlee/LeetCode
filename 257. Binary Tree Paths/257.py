class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        result = []

        def bfs(r, s):
            if s == '':
                s += str(r.val)
            else:
                s += '->' + str(r.val)
            if r.left is None and r.right is None:
                result.append(s)
                return
            if r.left:
                bfs(r.left, s)
            if r.right:
                bfs(r.right, s)

        if root:
            bfs(root, '')
        return result


if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)

    print(sol.binaryTreePaths(root))
